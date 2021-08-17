#!/bin/sh

wcxini=$1
target_root_directory=$2

parser=/opt/drivebadger/hooks/hook-wcxftp/filters/iniparser.py
$parser "$wcxini" |grep -iv ^default$ |grep -iv ^connections$ |grep -iv ^general$ |while read line; do

	if [ "`$parser "$wcxini" "$line" |grep ^password`" != "" ]; then
		ftphost=`$parser "$wcxini" "$line" host`
		ftpuser=`$parser "$wcxini" "$line" username`
		ftprawpass=`$parser "$wcxini" "$line" password`
		ftppass=`/opt/drivebadger/hooks/hook-wcxftp/filters/decode-totalcmd.py $ftprawpass`
		passive=`$parser "$wcxini" "$line" pasvmode`
		sharename=`echo "$line" |tr ' ' '_'`
		subtarget=$target_root_directory/ftp/$sharename/$ftphost
		mkdir -p $subtarget
		cd $subtarget

		logger "copying FTP share \"$line\" (found in $wcxini, target directory $subtarget)"

		if [ "$passive" = "1" ]; then
			pasv=""
		else
			pasv="--no-passive-ftp"
		fi

		wget $pasv --timeout=8 --tries=2 --mirror --ftp-user="$ftpuser" --ftp-password="$ftppass" --no-host-directories --preserve-permissions ftp://$ftphost/ >>$subtarget.log 2>>$subtarget.err &
	fi
done

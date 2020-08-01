#!/bin/sh

base=$1
remote_directory=$2

if [ -d "$base/Users" ]; then
	ls -1 "$base/Users" |grep -v desktop.ini |grep -v "All Users" |grep -v "Default User" |while read line; do
		wcxini="$base/Users/$line/AppData/Roaming/GHISLER/wcx_ftp.ini"
		if [ -f "$wcxini" ]; then
			logger "found $wcxini, processing possible ftp accounts"
			/opt/drives/hooks/ftp/handle-totalcmd.sh "$wcxini" $remote_directory
		fi
	done
fi

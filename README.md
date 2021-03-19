This is an extension for Drive Badger. It provides a so called hook script, that:

- scans given directory tree for `wcx_ftp.ini` files (with Total Commander FTP account configuration)
- analyzes its entries
- extracts all accounts with saved passwords
- decodes these passwords
- tries to exfiltrate these FTP accounts

Why this is done during the attack, and not later? Because:

- access to these FTP servers/accounts can be restricted to IP address of the exfiltrated computer/server
- FTP data transfers are logged - so this is a good way to cover the tracks

### Installing

Clone this repository as `/opt/drivebadger/hooks/hook-wcxftp` directory on your Drive Badger persistent partition.

### More information

- [Drive Badger main repository](https://github.com/drivebadger/drivebadger)
- [Drive Badger wiki](https://github.com/drivebadger/drivebadger/wiki)
- [description, how hook repositories work](https://github.com/drivebadger/drivebadger/wiki/Hook-repositories)

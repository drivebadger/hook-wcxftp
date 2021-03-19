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

#### Python 2.x

This particular extension uses Python 2.x to decode Total Commander passwords. It is tested to work with
Kali Linux version 2020.1b and should work without changes at least until 2020.3 - which is recent enough to support
all new hardware at least to the end of 2021, so the solution for now is just stay with Kali Linux 2020.3.

Later (2022 and so on), you will have to install any external Python 2.x distribution.

More information about transition to Python 3.x can be found [here](https://www.kali.org/docs/general-use/python3-transition/),
[here](https://www.kali.org/docs/general-use/using-eol-python-versions/) and [here](https://www.kali.org/blog/python-2-end-of-life/).

### More information

- [Drive Badger main repository](https://github.com/drivebadger/drivebadger)
- [Drive Badger wiki](https://github.com/drivebadger/drivebadger/wiki)
- [description, how hook repositories work](https://github.com/drivebadger/drivebadger/wiki/Hook-repositories)

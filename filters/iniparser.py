#!/usr/bin/env python

import sys
import configparser

if len(sys.argv) < 2:
	sys.exit(0)

config = configparser.ConfigParser()
config.read(sys.argv[1])

if len(sys.argv) > 3:
	print config[sys.argv[2]][sys.argv[3]]
elif len(sys.argv) > 2:
	print '\n'.join(config[sys.argv[2]])
else:
	print '\n'.join(config)

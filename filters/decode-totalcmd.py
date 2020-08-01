#!/usr/bin/env python
"""
Copyright (C) <2013> <Csaba Fitzl>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


Cloned from https://github.com/theevilbit/tcpwrecovery and simplified by Tomasz Klim for easy usage as a command line filter for encrypted passwords, with absolutely minimal dependencies.
"""

import sys

def tc_random(nMax):
	global RANDOM_BASE
	RANDOM_BASE = ((RANDOM_BASE * 0x8088405) & 0xffffffff) + 1
	return (((RANDOM_BASE * nMax) >> 32) & 0xffffffff)

def tc_shift(n1, n2):
	return (((n1 << n2) & 0xffffffff) | ((n1 >> (8 - n2)) & 0xffffffff)) & 0xff

def tc_decrypt(pwd):
	global RANDOM_BASE
	password=[]
	for i in range(len(pwd)/2 - 4): #skip last 8 characters (4 * 2 bytes)
		password.append(int(pwd[2*i:2*(i+1)],16))
	pwlen = len(password)

	RANDOM_BASE = 849521
	for i in range(pwlen):
		password[i] = tc_shift(password[i], tc_random(8))

	RANDOM_BASE = 12345
	for i in range(256):
		a=tc_random(pwlen)
		b=tc_random(pwlen)
		password[a],password[b] = password[b],password[a]

	RANDOM_BASE = 42340
	for i in range(pwlen):
		password[i] = (password[i] ^ tc_random(256)) & 0xff

	RANDOM_BASE = 54321
	for i in range(pwlen):
		password[i] = (password[i] - tc_random(256)) & 0xff

	for i in range(pwlen):
		password[i] = chr(password[i])

	return "".join(password)

def main():
	if len(sys.argv) > 1 and len(sys.argv[1]) > 2:
		if ("password" in sys.argv[1].strip()):
			print tc_decrypt(sys.argv[1].strip().split("=")[1])
		else:
			print tc_decrypt(sys.argv[1])

if __name__ == '__main__':
	main()

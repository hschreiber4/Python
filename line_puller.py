#!/usr/bin/env python

#This script pulls lines from a file that contains a search term loaded from a second file.

import sys as s


names = open(s.argv[2]).readlines()
for line in open (s.argv[1]):
	for name in names:
		if name.rstrip('\n') in line:
			print line,
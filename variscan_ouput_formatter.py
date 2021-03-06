#!/usr/bin/env python

from sys import *

infile = open (argv[1])
outfile = open ("Format_"+argv[1].split('_')[1], "wt")

outfile.write("Midpoint\tPi\n")
for line in infile:
	if line.startswith("#"):
		pass
	else:
		lineparts= line.split(" ")
		fixed = [x.strip(" ") for x in lineparts]
		full = [y for y in fixed if y != '']
		if "nan" in full:
			pass
		else:
			outfile.write("{0}\t{1}\t{2}\n".format(argv[1].split('_')[1],full[5],full[11]))


infile.close()
outfile.close()
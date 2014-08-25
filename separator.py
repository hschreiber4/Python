#!/usr/bin/env python
import sys
import os


infile=open(sys.argv[1])
lines=infile.readlines()
while len(lines)!=0:
	line=lines.pop(0)
	if line.startswith('>'):
		line=line.rstrip("\n")
		filename=line.split(', ')[1]+".fasta"
		outfile=open(filename, 'wt')
		outfile.write("{:s}\n".format(line))
		# while len(templines)!=0:
		# 	templine=templines.pop(0)
		# 	if templine.startswith(">"):
		# 		break
		# 	outfile.write(templine)
		for seqline in lines:
			if seqline.startswith(">"):
				break
			outfile.write(seqline)
		outfile.close()
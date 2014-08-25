#!/usr/bin/env python

import os
import sys


for item in os.listdir(sys.argv[1]):
	if item.endswith('.cds'):
		infile=open (item)
		outfile=open(item.replace('.cds','2.cds'),'wt')
		for line in infile:
			if line.startswith('>'):
				newitem=item.replace 
				outfile.write('>'+str(item.split('_POSTPRODIGAL')[0])+'::'+line.lstrip('>'))
			else:
				outfile.write(line)
#Here are all my imports
import re
import sys

#Hard coding the input file for easier coding to start with
for line in open('short_file.txt'):
	item = line.split(' ')
	for portion in item:
		print portion
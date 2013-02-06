#NOTE NOTE NOTE NOTE
#This script is deprecated.  glimmer_orf_extraction.py replaces this funcitonality into one script.

#This program will take the predicted coordinates from a Glimmer3.02 run on a multi-fasta file and turn it into the proper format for the multi-extract feature of the program.

print ('Lets start choppin\'')

import re
import sys


#A usage statement to tell the user how to use the script
if len(sys.argv)!=3:
	print '\n'+'\n'+'\n'+'To use this script, type: python multi_extract.processor.py {input .predict file} {output .predict file}'+'\n'
	if len(sys.argv)<3:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>3:
		print 'You added something!'+'\n'
	sys.exit()

#Lets load the input file!
infile = open (sys.argv[1])
if infile == 0:
	print ('There is a problem with the input file')
	sys.exit()

outfile = open (sys.argv[2],'wt')
if outfile ==0:
	print ('There is a problem with the output file')
	sys.exit()

#Lets read the file, line by line for greater tractability of the information
while True:

	line = infile.readline().rstrip()
	if re.search('>',line):
		header = line.strip('>')
		continue
	
	#When the file runs out of lines, end the while loop
	if line == (''):
		break

	else:
		split = line.split()
		if split != 1:
			combined = split[0] + '     ' + header + '     ' + split[1] + '     ' + split[2]  + '     ' + split[3]  + '     ' + split[4] + '\n'
			outfile.write(combined)

outfile.close()
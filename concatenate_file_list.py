import sys
import subprocess
import os
import re

#This program is meant to concatenate all the FASTA files made from glimmer_orf_extraction.py script.  Must use GREP to rewrite the header sequences.  With a little work, this could be turned into a full-fledged package with a single run.

#Usage statements
if len(sys.argv)!=3:
    print '\n'+'\n'+'\n'+'To use this script, type: concatenate_file_list.py {input directory[full path]} {output file}'+'\n'
    if len(sys.argv)<3:
        print 'You forgot something!'+'\n'
    elif len(sys.argv)>3:
        print 'You added something!'+'\n'
    sys.exit()


#Loads files in directory into a list
files = os.listdir(sys.argv[1])
print files

#Opens each file
for filename in files:
	if filename.endswith('.fa'):
		filestrip=filename.rstrip('.fa')
		print 'Working on '+filestrip
		
		#Load the file
		infile=open(filename)
		print infile
		if infile == 0:
			print ('There is a problem with the input file')
    		sys.exit()

    	#Opens the writing directory
		outfile=open(sys.argv[2],'a')
		if outfile ==0:
			print ('There is a problem with the output file')
			sys.exit()

		#Lets read the file, line by line for greater tractability of the information
		while True:
			print infile
			line = infile.readline()
			print line
			if line == (''):
				break
			else:
				outfile.write('ANYTHING')
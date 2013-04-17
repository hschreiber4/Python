import sys
import os
import re

print '\n\n\n'+'This script will take the blastn results file from a directory, split the results file by strain, and concatenates the sequences.  The results are FASTA files with the strain name at the top, and a list of the sequences following it, and then the sequence itself\n\n\nThis script is meant for E5B2 - Sequencing of Clinical Isolates.\n'

#A usage statement to tell the user how to use the script
if len(sys.argv)!=2:
	print '\n'+'\n'+'\n'+'To use this script, type: python batch_blastn.py {directory of blastn sequences[USE THE FULL PATH WITH NP END SLASH]}'+'\n'
	if len(sys.argv)<3:
		print 'You forgot something!'+'\n'
	sys.exit()


#This section loads the files.
files = os.listdir(sys.argv[1])

#Empty variables
d={}
i=0
k=0

#Iterates through the files in the directory and only works with those that have the proper format
for item in files:
	if item.endswith('.txt'):
		infile = open (sys.argv[1]+'/'+item)
		
		#This lets you print the name so that you can know what order the blastn files were processed.
		print 'Working on '+item

		#This counter section was necessary to fill the dict so that we could then append sequences to it later.
		i+=1
		if i == 1:
			for line in infile:
				#After splitting the name, the update command is used to fill the dict with the key set to the strain name and the value set to the sequence.
				name=line.split('\t')[0]
				d.update({name.split('_')[0]:[line.split('\t')[10]]})

				#This section appends sequences from the remaining blastn files to their appropriate dict key (or strain name, in this case)
		else:
			for line in infile:
				name=line.split('\t')[0]
				d[name.split('_')[0]].append(line.split('\t')[10])
				
#This prints the output.  Great success!
for key in d:
	new = ''.join(d[key])
	edited=new.replace('\n','')
	print '>'+key
	print edited
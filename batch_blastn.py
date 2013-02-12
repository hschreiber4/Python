import sys
import subprocess
import os
import re

print '\n\n\n'+'This program will call all the query FASTA sequences in a directory and pass them through the blastn command of blast+.\n\n\nThis script is meant for E5B2 - Sequencing of Clinical Isolates.'+'\n'

#A usage statement to tell the user how to use the script
if len(sys.argv)!=3:
	print '\n'+'\n'+'\n'+'To use this script, type: python batch_blastn.py {directory of query sequences[USE THE FULL PATH WITH NO END SLASH]} {output directory [USE THE FULL PATH AND NO END SLASH}'+'\n'
	if len(sys.argv)<3:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>3:
		print 'You added something!'+'\n'
	sys.exit()

#This section loads the files.
files = os.listdir(sys.argv[1])

#Starting the loop to look for files.
for filename in files:
	if filename.endswith('.fa'):
		print 'Working on '+filename.rstrip('.fa')

		# #Setting the blastn command
		# blastn_cmd='blastn -db UPEC_TOP_ORFS_db -query '+sys.argv[1]+'/'+filename+' -outfmt "6 sseqid evalue bitscore pident qlen slen qstart qend sstart send sseq">'+sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt'
		# subprocess.call(blastn_cmd, shell=True)

		#Ediitng the file to take out the spurious results
		if os.path.exists(sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')==True:
			print 'blastn results file created for'+filename.rstrip('.fa')
			infile = open (sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')
			outfile = open (sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results_edited.txt', 'wt')

			id_list=[]	
			orf_list=[]
			for line in infile:
				line_parts=line.split('\t')
				id_parts=line_parts[0].split('_')
				if any(id_parts[0] in s for s in id_list):
					continue
				else:
					outfile.write(line)
				id_list.append(id_parts[0])
				orf_list.append(id_parts[1])
				

				#This section writes to the file unless the length of the ORF matched by the query is much longer than the subject query, which is an indication of a spurious result.  This arises because glimmer contains predicted genes within other genes, which is not good news.
				# limit= int(line_parts[4])+1000
				# if int(line_parts[5])<int(limit):
				# 	outfile.write(line)
					
		#Killing the program if it doesn't make the file.
		# else os.path.exists(sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')==False:
		# 	print 'There was a problem making the blastn results file for '+filename.rstrip('.fa')
		# 	sys.exit()
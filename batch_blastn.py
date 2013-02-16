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

#This counter and list will be used in the construction of the presence/absence table for the genes
strain_list=['11.1a', '21.1a', '35.3r', '9.2p', '11.2p', '21.2p', '41.1a', '9.3r', '11.3r', '21.3r', '41.2p', 'ABU', '12.1a', '2.1a', '41.3r', 'APEC', '12.2p', '2.2r', '41.4p', 'CFT073', '12.3r', '26.1a', '41.5r', 'E24377A', '12.4r', '26.2p', '5.1a', 'IAI39', '13.2p', '26.3r', '5.2p', 'MG1655', '13.4p', '31.1a', '536', 'O157', '17.1a', '31.2p', '5.3r', 'S88', '17.2p', '31.3r', '55989', 'UTI89', '17.3r', '34.1a', '56.1r', 'UTI89', '20.1a', '34.2r', '56.2r', '20.2r', '35.1a', '56.3r', '20.3r', '35.2p', '9.1a']

#The results file will contain data on the presence or absence of genes from the genomes
results_file = open ('Restults.txt','wt')
results_file.write('StrainIDs')
for strain in strain_list:
	results_file.write('\t'+strain)


#Starting the loop to look for files.
for filename in files:
	if filename.endswith('.fa'):
		print 'Working on '+filename.rstrip('.fa')

		# #Setting the blastn command
		blastn_cmd='blastn -db UPEC_TOP_ORFS_db -query '+sys.argv[1]+'/'+filename+' -outfmt "6 sseqid evalue bitscore pident qlen slen qstart qend sstart send sseq">'+sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt'
		subprocess.call(blastn_cmd, shell=True)

		#Ediitng the file to take out the spurious results
		if os.path.exists(sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')==True:
			print 'blastn results file created for '+filename.rstrip('.fa')
			infile = open (sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')
			outfile = open (sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results_edited.txt', 'wt')
			
			#Let's write some headers!
			outfile.write('SubjectID\tEvalue\tBitscore\tPercentID\tQueryLength\tSubjectLength\tQueryStart\tQueryEnd\tSubjectStart\tSubjectEnd\tSubjectSeq\n')

			#This section will remove hits from ORFs that are not meant to be there in the first place, due to glimmer's idiosyncracies.
			for line in infile:
				line_parts = line.split('\t')
				limit= int(line_parts[4])*2
				if int(line_parts[5])<int(limit):
					strain_list.append(line_parts[0].split('_')[0])
					outfile.write(line)

			
			print 'blastn results file edited for '+filename.rstrip('.fa')
			infile.close()


		#Killing the program if it doesn't make the file.
		if os.path.exists(sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')==False:
			print 'There was a problem making the blastn results file for '+filename.rstrip('.fa')
			sys.exit()
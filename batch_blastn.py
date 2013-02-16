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
strain_list=['UTI89-NCBI', 'UTI89', 'S88-NCBI', 'APECO1-NCBI', '5.3r', '5.2p', '34.2r', '34.1', '31.3r', '536-NCBI', '35.3r', '35.2p', '35.1', '21.3r', '21.2p', '21.1', '20.3r', '20.2r', '20.1', '41.3r', '41.2p', '41.1', 'CFT073-NCBI', 'ABU83972-NCBI', '56.3r', '56.2r', '17.3r', '17.2p', '17.1', '26.3r', '26.2p', '26.1', '13.4p', '13.2p', '12.4r', '12.3r', '12.2p', '12.1', 'E24377A-NCBI', '9.3r', '9.2p', '56.1r', '5.1', '41.5r', '41.4p', '31.2p', '55989-NCBI', 'EC4115-NCBI', 'MG1655-NCBI', '11.3r', '11.2p', '11.1a.fa', '31.1', '9.1', '2.2r', 'IAI39-NCBI', '2.1']
strain_list.sort()

#The results file will contain data on the presence or absence of genes from the genomes
results_file = open ('Results.txt','wt')
results_file.write('StrainIDs')
for strain in strain_list:
	results_file.write('\t'+strain)

#Starting the loop to look for files.
for filename in files:
	if filename.endswith('.fa'):
		id_list=[]
		duplicate_checklist=[]
		print 'Working on '+filename.rstrip('.fa')

		# #Setting the blastn command
		# blastn_cmd='blastn -db UPEC_TOP_Genomes_db -query '+sys.argv[1]+'/'+filename+' -outfmt "6 sseqid evalue bitscore pident qlen slen qstart qend sstart send sseq">'+sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt'
		# subprocess.call(blastn_cmd, shell=True)

		#Checking to see if file exists
		if os.path.exists(sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')==True:
			print 'blastn results file created for '+filename.rstrip('.fa')

			#Adding the file tested to the Results section
			results_file.write('\n'+filename.rstrip('.fa'))
			
			#This section will search the orfs and put the presence or absence in a blastn results file
			infile = open (sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')
			for line in infile:
				line_parts=line.split('\t')
				id_parts = line_parts[0].split('_')
				id_list.append(id_parts[0])
				id_list.sort()

			print filename.rstrip('.fa')+' is found in the genomes '+str(id_list)

			for name in id_list:
				# for dup in duplicate_checklist:
				# 	if name in dup:
				# 		results_file.write('**NEEDS ATTENTION**')
				if name in s for s in strain_list:
					results_file.write('\t1')
				else:
					results_file.write('\t0')
				duplicate_checklist.append(name)


		# #Killing the program if it doesn't make the file.
		# if os.path.exists(sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')==False:
		# 	print 'There was a problem making the blastn results file for '+filename.rstrip('.fa')
		# 	sys.exit()
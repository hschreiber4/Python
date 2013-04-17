import sys
import subprocess
import os
import re

print '\n\n\n'+'This program will call all the query FASTA sequences in a directory and pass them through the blastn command of blast+.\n\n\nThis script is meant for E5B2 - Sequencing of Clinical Isolates.'+'\n'

#A usage statement to tell the user how to use the script
if len(sys.argv)!=3:
	print '\n'+'\n'+'\n'+'To use this script, type: python batch_blastn_UPEC_db.py {directory of query sequences[USE THE FULL PATH WITH NO END SLASH]} {output directory [USE THE FULL PATH AND NO END SLASH}'+'\n'
	if len(sys.argv)<3:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>3:
		print 'You added something!'+'\n'
	sys.exit()

#This section loads the files.
files = os.listdir(sys.argv[1])

#The results file will contain data on the presence or absence of genes from the genomes
results_file = open ('Results.txt','wt')
results_file.write('StrainIDs')

strain_dict={'11.1a':0, '20.2r':0, '41.3r':0, '11.2p':0, '20.3r':0, '41.4p':0, '11.3r':0, '21.1a':0, '41.5r':0, '12.1a':0, '21.2p':0, '5.1a':0, '12.2p':0, '21.3r':0, '5.2p':0, '12.3r':0, '26.1a':0, '5.3r':0, '12.4r':0, '26.2p':0, '536':0, '13.1a':0, '26.3r':0, '56.1r':0, '13.2p':0, '31.1a':0, '56.2r':0, '13.3r':0, '31.2p':0, '56.3r':0, '13.4p':0, '31.3r':0, '9.1a':0, '34.1a':0, '9.2p':0, '17.1a':0, '34.2r':0, '9.3r':0, '17.2p':0, '35.1a':0, 'CFT073':0, '17.3r':0, '35.2p':0, 'UTI89-NCBI':0, '2.1a':0, '35.3r':0, 'UTI89':0, '2.2r':0, '41.1a':0, '20.1a':0, '41.2p':0}

strain_list=strain_dict.keys()
strain_list.sort()	
for name in strain_list:	
	results_file.write('\t'+name)

#Starting the loop to look for files.
for filename in files:
	if filename.endswith('.fa'):
		print 'Working on '+filename.rstrip('.fa')

		#Setting the blastn command
		blastn_cmd='blastn -db UPEC_Genomes_db -query '+sys.argv[1]+'/'+filename+' -outfmt "6 sseqid evalue bitscore pident qlen slen qstart qend sstart send sseq">'+sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt'
		subprocess.call(blastn_cmd, shell=True)

		#Checking to see if file exists
		if os.path.exists(sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')==True:
			print 'blastn results file created for '+filename.rstrip('.fa')
			#This dict will be used in the construction of the presence/absence table for the genes
			strain_dict={'11.1a':0, '20.2r':0, '41.3r':0, '11.2p':0, '20.3r':0, '41.4p':0, '11.3r':0, '21.1a':0, '41.5r':0, '12.1a':0, '21.2p':0, '5.1a':0, '12.2p':0, '21.3r':0, '5.2p':0, '12.3r':0, '26.1a':0, '5.3r':0, '12.4r':0, '26.2p':0, '536':0, '13.1a':0, '26.3r':0, '56.1r':0, '13.2p':0, '31.1a':0, '56.2r':0, '13.3r':0, '31.2p':0, '56.3r':0, '13.4p':0, '31.3r':0, '9.1a':0, '34.1a':0, '9.2p':0, '17.1a':0, '34.2r':0, '9.3r':0, '17.2p':0, '35.1a':0, 'CFT073':0, '17.3r':0, '35.2p':0, 'UTI89-NCBI':0, '2.1a':0, '35.3r':0, 'UTI89':0, '2.2r':0, '41.1a':0, '20.1a':0, '41.2p':0}
			#This list is emptied in each file to be loaded by the hits.
			id_list=[]
			#Adding the file tested to the Results section
			results_file.write('\n'+filename.rstrip('.fa'))
			
#This section will search the orfs and put the presence or absence in a blastn results file
			
			#This code bit makes a list of the strain names in the blastn results file you are working with
			infile = open (sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')
			for line in infile:
				line_parts=line.split('\t')
				id_parts = line_parts[0].split('_')
				id_list.append(id_parts[0])
				
			#This bit of code will note any time that there was a blastn hit that matches the strains identified.
			for id_name in id_list:
				strain_dict[id_name]+=1

			# This bit prints the code to a results file that will tell you if there has been a match to the strains that you are interested in.
			for strain_name in strain_list:
				if strain_dict[strain_name]==1:
					results_file.write('\t1')
				if strain_dict[strain_name]==0:
					results_file.write('\t0')
				if strain_dict[strain_name]>1:
					results_file.write('\tMultiple Hits')




		#Killing the program if it doesn't make the file.
		if os.path.exists(sys.argv[2]+'/'+filename.rstrip('.fa')+'_blastn_results.txt')==False:
			print 'There was a problem making the blastn results file for '+filename.rstrip('.fa')
			sys.exit()
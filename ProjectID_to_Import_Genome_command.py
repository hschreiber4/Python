#This script takes strain names and project numbers given in a separate file and produces an output file of commands that can be used to load genomes into Calhoun. As part of this process, the accession numbers for each plamid and chromosome associated with a project ID are retrieved, in addition to the identification of the strain name from NCBI. Both of these processes use eutilities from NCBI.

#The input file should be loaded as such:
#[YOUR STRAIN NAME][TAB][PROJECT ID][NEWLINE]
#[YOUR STRAIN NAME][TAB][PROJECT ID][NEWLINE]

#The output file will contain a shebang for bash, and then will have commands in the following format:
#/seq/annotation/prod/calhoun/bin/calhoun job dbio.insertAssemblyFromGenbank [YOUR STRAIN NAME] [ACCESSION NUMBERS] [CELL TYPE] --accession=[ACCESSION NUMBERS] --strainName=[NCBI STRAIN NAME] --cellType=[CELL TYPE] --groupName=[YOUR STRAIN NAME][NEWLINE]

import sys
import subprocess
import os
import re

#######Standard Options########
cell_type = 'P'
method="--useGiList=true"
################################



print 'This script will create a file containing commands to import genomes into Calhoun\n'

#A usage statement to tell the user how to use the script
if len(sys.argv)!=3:
	print '\n'+'\n'+'\n'+'To use this script, type: [SCRIPT NAME][INPUT FILE] [OUTPUT FILE]\n'
	if len(sys.argv)<3:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>3:
		print 'You added something!'+'\n'
	sys.exit()
#Setting variables
project_id=[]
d={}

#Loading the input information
infile = open(sys.argv[1])
for line in infile:
	split_line = line.split('\t')
	project_id.append(split_line[1].replace('\n',''))
	d[split_line[1].replace('\n','')]=split_line[0]

#PREPARE OUTPUT FILE
outfile = open (sys.argv[2],'wt')
outfile.write('#!/bin/bash\n')

#Retrieving information from NCBI using eutilities
for item in project_id:
	gi_list=[]
	search_cmd='curl \"http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&term='+item+'\" > '+item+'_search.txt'
	subprocess.call(search_cmd, shell = True)
	search_file = open (item+'_search.txt')
	for line in search_file:
		if line.startswith('<Id>'):
			gi_number=line.replace('<Id>','').replace('</Id>','').replace('\n','')
			gi_list.append(gi_number)
	finished_gi=','.join(gi_list)

	fetch_cmd='curl \"http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id='+gi_list[0]+'&rettype=gb\" > '+item+'_fetch.txt'
	subprocess.call(fetch_cmd, shell = True)
	fetch_file = open (item+'_fetch.txt')
	for line in fetch_file:
		if re.search('/strain', line):
			split_line = line.split('=')
			strain_id = split_line[1].replace('\"','').replace('\n','').replace(' ','-')

	#Writes commands
	outfile.write('/seq/annotation/prod/calhoun/bin/calhoun job dbio.insertAssemblyFromGenbank '+d[item]+' '+finished_gi+' '+cell_type+' --accession='+finished_gi+' --strainName='+strain_id+' --cellType='+cell_type+' --groupName='+d[item]+' '+method+'\n')
	os.remove(item+'_search.txt')
	os.remove(item+'_fetch.txt')

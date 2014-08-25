#!/usr/bin/env python

import os
import subprocess
import sys
import collections

genomecount={}
hitcount={}
single={}
multiple={}

if len(sys.argv)!=3:
	print "To use this script, type [SCRIPT NAME] [PATH/TO/DIRECTORY of Query Peptide Sequences] [PATH/TO/BLAST DATABASE]"
	sys.exit()

for query in os.listdir(sys.argv[1]):
	if query.endswith('.fasta'):
		print 'Working on '+query
		cmd = 'blastn -db '+sys.argv[2]+' -query '+sys.argv[1]+query+' -perc_identity 0.80 -max_target_seqs 95 -outfmt "6 sseqid evalue bitscore pident length qlen" -out intermediate.txt'
		subprocess.call(cmd, shell=True)

		outfile=open (query.rstrip('.fasta')+'_results.txt', 'wt')
		i=0
		hitcount[query]=0
		
		for line in open('intermediate.txt'):
			lineparts=line.split('\t')
			coverage=float(lineparts[4])/float(lineparts[5])
			if float(lineparts[3])>=80 and coverage>=0.50:
				outfile.write(line)

				if lineparts[0] in single:
					multiple[lineparts[0]] = single[lineparts[0]]+'\t'+query+' '+str(lineparts[3])+' '+str(coverage)
					parts=single[lineparts[0]]
					first_id=parts.split(' ')[1]
					first_cov=parts.split(' ')[2]
					if (float(lineparts[3])*coverage)>(float(first_id)*float(first_cov)):
						single[lineparts[0]]=query+' '+str(lineparts[3])+' '+str(coverage)
					if (float(lineparts[3])*coverage)<(float(first_id)*float(first_cov)):
						pass
				else:
					single[lineparts[0]]=query+' '+str(lineparts[3])+' '+str(coverage)
					genomecount[lineparts[0].split(':')[0]]=0

				i=1
		if i!=1:
			os.remove(query.rstrip('.fasta')+'_results.txt')
		
		outfile.close()


singlefile=open ('single_hits.txt','wt')
osingle=collections.OrderedDict(sorted(single.items()))
for k, v in osingle.iteritems():
	genomecount[k.split(':')[0]]+=1
	singlefile.write(k+'\t'+v+'\n')
	hitcount[v.split(' ')[0]]+=1

multiplefile= open ('multiple_hits.txt','wt')
omultiple=collections.OrderedDict(sorted(multiple.items()))
for k, v in omultiple.iteritems():
	multiplefile.write(k+'\t'+v+'\n')

genome_hitfile=open('genome_hits.txt','wt')
ogenomecount=collections.OrderedDict(sorted(genomecount.items()))
for k, v in ogenomecount.iteritems():
	genome_hitfile.write(k+'\t'+str(v)+'\n')

protein_hitfile=open ('protein_hits.txt','wt')
ohitcount=collections.OrderedDict(sorted(hitcount.items()))
for k, v in ohitcount.iteritems():
	protein_hitfile.write(k+'\t'+str(v)+'\n')

os.remove('intermediate.txt')
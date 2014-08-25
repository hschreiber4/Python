import subprocess
import sys

d={}
for line in open (sys.argv[1]):
	line=line.strip('\n ')
	d[line.split('\t')[0]]=line.split('\t')[1]

for item in d:
	cmd='curl -o '+d[item]+'.fa -s http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore\&id='+item+'\&rettype=fasta'
	print cmd
	subprocess.call(cmd, shell=True)
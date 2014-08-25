import re
import sys

#A usage statement to tell the user how to use the script
if len(sys.argv)!=5:
	print '\n'+'\n'+'\n'+'To use this script, type: python [SCRIPT NAME] [ANNOTATION FILE] [DATABASE FILE] [DIRECTORY OF CDS FILES] [SEARCH TERM]\n'
	if len(sys.argv)<5:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>5:
		print 'You added something!'+'\n'
	sys.exit()

#Setting variables
annotation_file=sys.argv[1]
database_file=sys.argv[2]
directory_of_cdsfiles=sys.argv[3]
search_term=sys.argv[4]

d={} #Dictionary of CDS tags from each genome
for line in open (database_file):
	d[line.split('\t')[0]]=line.split('\t')[1].rstrip('\n')

cdslist=[]	#The list of the CDS tags associated with search term
for line in open (annotation_file):
	if search_term in line:
		cdstag=line.split('\t')[0]
		if cdstag not in cdslist:
			cdslist.append(cdstag)

#Does the crossreferencing
for item in cdslist:
	outfile=open(item+'_renamed.fa','wt')
	for line in open (directory_of_cdsfiles+item+'.cds'):
		line=line.strip('\n') #Remove extra new line characters
		if line.startswith('>'):
			cdstag=line.strip('>')
			if cdstag in d:
				outfile.write(line.replace(cdstag,d[cdstag])+'\n')
			else:
				outfile.write(line+'\n')
		else:
			outfile.write(line+'\n')
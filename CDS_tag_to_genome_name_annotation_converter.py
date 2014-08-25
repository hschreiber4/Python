import sys
import os

#A usage statement to tell the user how to use the script
if len(sys.argv)!=3:
	print '\n'+'\n'+'\n'+'To use this script, type: python [SCRIPT NAME] [DATABASE FILE] [DIRECTORY OF CDS FILES]\n'
	if len(sys.argv)<3:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>3:
		print 'You added something!'+'\n'
	sys.exit()

d={} #Dictionary of CDS tags from each genome
for line in open (sys.argv[1]):
	d[line.split('\t')[0]]=line.split('\t')[1].rstrip('\n')

#Does the crossreferencing
for item in os.listdir(sys.argv[2]):
	if item.endswith('.cds'):
		for line in open (item):
			line=line.strip('\n') #Remove extra new line characters
			if line.startswith('>'):
				cdstag=line.strip('>')
				if cdstag in d:
					print line.replace(cdstag,d[cdstag])
				else:
					print line
			else:
				print line
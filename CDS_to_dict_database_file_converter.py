import sys
import os

#A usage statement to tell the user how to use the script
if len(sys.argv)!=2:
	print '\n'+'\n'+'\n'+'To use this script, type: python batch_blastn.py directory of CDS files\n'
	if len(sys.argv)<2:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>2:
		print 'You added something!'+'\n'
	sys.exit()

for cds_file in os.listdir(sys.argv[1]):
	if cds_file.endswith('.cds'):
		format_name1 = cds_file.replace('_POSTPRODIGAL_1.annotation.cds','')
		format_name2 = format_name1.replace('_POSTPRODIGAL_2.annotation.cds','')
		format_name = format_name2.replace('_POSTPRODIGAL_3.annotation.cds','')
		for line in open (cds_file):
			if line.startswith('>'):
				lineparts = line.split(' ',3)
				print lineparts[0].lstrip('>')+'\t'+format_name+' '+lineparts[3].rstrip('\n')
import sys
import os

if len(sys.argv)!=2:
	print '\n'+'\n'+'\n'+'To use this script, type: python rename.py {directory of query sequences[USE THE FULL PATH WITH NO END SLASH]}'
	if len(sys.argv)<2:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>2:
		print 'You added something!'+'\n'
	sys.exit()

file_list=os.listdir(sys.argv[1])

for item in file_list:
	if item.endswith('.fa'):
		infile = open (item)
		outfile = open (item.rstrip('.fa')+'_formatted.fa', 'wt')
		for line in infile:
			if line.startswith('>'):
				line = '>'+item.rstrip('.fa')+'_'+line.lstrip('>')
				outfile.write(line)
			else:
				outfile.write()



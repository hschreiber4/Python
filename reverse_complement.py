import sys
import string

#A usage statement to tell the user how to use the script
if len(sys.argv)!=2:
	print '\n'+'\n'+'\n'+'To use this script, type: python GFF3_edit.py {input file}\n'
	if len(sys.argv)<2:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>2:
		print 'You added something!'+'\n'
	sys.exit()

#Lets load the input file!
infile = open (sys.argv[1])
if infile == 0:
	print ('There is a problem with the input file')
	sys.exit()

for line in infile:
	if line.startswith('>'):
		print line.replace('\n','')
	else:
		# print line
		# print line[::-1]
		print line[::-1].upper().translate(string.maketrans('ACTG','TGAC'))


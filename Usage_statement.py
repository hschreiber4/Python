#A usage statement to tell the user how to use the script
if len(sys.argv)!=3:
	print '\n'+'\n'+'\n'+'To use this script, type: python {scriptname} {input} {output}'+'\n'
	if len(sys.argv)<3:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>3:
		print 'You added something!'+'\n'
	sys.exit()

#Lets load the input file!
infile = open (sys.argv[1])
if infile == 0:
	print ('There is a problem with the input file')
	sys.exit()

outfile = open (sys.argv[2],'wt')
if outfile ==0:
	print ('There is a problem with the output file')
	sys.exit()
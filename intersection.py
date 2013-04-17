import sys
#A usage statement to tell the user how to use the script
if len(sys.argv)!=3:
	print '\n'+'\n'+'\n'+'To use this script, type: python intersection.py {the name of the input file} {name of results file}\n'
	if len(sys.argv)<4:
		print 'You forgot something!'+'\n'
	sys.exit()

infile = open(sys.argv[1])
otherlines=infile.readlines()
infile.close()
results_file = open (sys.argv[2],'wt')

total=0
intersection=0
i=0

infile2 = open(sys.argv[1])
for line in infile2:
	i+=1
	if i==1:
		pass
	else:
		line=line.replace('\n','')
		a=line.split('\t')
		nameA=a.pop(0)
		results_file.write('\n'+nameA)

		j=0
		for item in otherlines:
			j+=1
			if j==1:
				continue
			else:
				item=item.replace('\n','')
				b=item.split('\t')
				nameB=b.pop(0)
				
				total=0
				intersection=0

				zipped = zip(a,b)
				for thing in zipped:
					if int(thing[0])==1 or int(thing[1])==1:
						total+=1.0
						if thing[0]==thing[1]:
							intersection+=1.0
				jacard_coeff=intersection/total
				results_file.write('\t'+str(jacard_coeff))
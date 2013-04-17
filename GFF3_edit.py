import sys
import re


print '\n\nThis script is for Phage Hunters Bio192 and can be used to take a .GFF3 file that has only the \'gene\' line entries.  This will add the mRNA and exon line entries\n\n\n\n'

#A usage statement to tell the user how to use the script
if len(sys.argv)!=3:
	print '\n'+'\n'+'\n'+'To use this script, type: python GFF3_edit.py {input .GFF3 file} {output .GFF3 file}'+'\n'
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

#iterates through the line, skips the first line of the file that has the ##gff label
for line in infile:
	if re.search('#',line):
		outfile.write(line.rstrip()+'\n')
	
#There is probably a much prettier way of doing this, but this is functional.  This bit of code will split the line by tabs, then isolate the important information with splits to '=' and ';'.  I take the middle name instead of the name at the end so that I don't have to worry about the annoying end of line characters.
	else:
		line=line.rstrip()
		split_line=line.split('\t')
		pre1_name=split_line.pop()
		pre2_name=pre1_name.split('=')
		name=pre2_name[1].split(';')
		if line.endswith('\n'):
			outfile.write(line)
			outfile.write(split_line[0]+'\t'+split_line[1]+'\tmRNA\t'+split_line[3]+'\t'+split_line[4]+'\t'+split_line[5]+'\t'+split_line[6]+'\t'+split_line[7]+'\tID='+name[0]+'.mRNA;Parent='+name[0]+'\n')
			outfile.write(split_line[0]+'\t'+split_line[1]+'\texon\t'+split_line[3]+'\t'+split_line[4]+'\t'+split_line[5]+'\t'+split_line[6]+'\t'+split_line[7]+'\tID='+name[0]+'.exon;Parent='+name[0]+'.mRNA\n')
		else:
			outfile.write(line+'\n')
			outfile.write(split_line[0]+'\t'+split_line[1]+'\tmRNA\t'+split_line[3]+'\t'+split_line[4]+'\t'+split_line[5]+'\t'+split_line[6]+'\t'+split_line[7]+'\tID='+name[0]+'.mRNA;Parent='+name[0]+'\n')
			outfile.write(split_line[0]+'\t'+split_line[1]+'\texon\t'+split_line[3]+'\t'+split_line[4]+'\t'+split_line[5]+'\t'+split_line[6]+'\t'+split_line[7]+'\tID='+name[0]+'.exon;Parent='+name[0]+'.mRNA\n')

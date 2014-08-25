#!/Library/Frameworks/Python.framework/Versions/Current/bin/python
import sys
import subprocess

print 'Hello\nThis command will curl all downloadable items from a PHAST search based on an input list\n\n\n'

#########NOTE ON INPUT FILE###########
#The input file should be in the following format
#[PHAST ID NUMBER][TAB][YOUR STRAIN NAME]
#Brackets are unnecessary

#The data_list can be changed if you want to download different files
data_list=['summary.txt', 'detail.txt', 'image.png', 'region_DNA.txt', 'true_defective_prophage.txt', 'png_input', 'extract_RNA_result.txt.tmp']

phast_id=[]
d={}
#Formats the input file.
infile = open(sys.argv[1])
for line in infile:
	split_line = line.split('\t')
	phast_id.append(split_line[0])
	d[split_line[0]]=split_line[1].replace('\n','')

#Formats and runs the code
for ID in phast_id:
	print 'Retrieving data for '+d[ID]
	for item in data_list:
		cmd='curl -s -S -o '+d[ID]+'_'+item+' http://phast.wishartlab.com/tmp/'+ID+'/'+item
		subprocess.call(cmd, shell=True)
		glimmercmd='curl -s -S -o '+d[ID]+'_glimmer.predict http://phast.wishartlab.com/tmp/'+ID+'/'+ID+'.predict'
		subprocess.call(glimmercmd, shell=True)
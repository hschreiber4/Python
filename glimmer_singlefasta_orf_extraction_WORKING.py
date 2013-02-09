import sys
import subprocess
import os
import re

print '\n\n\n'+'This program will call fall in a directory and pass them through Glimmer and multi-extract.  This script is meant for E5B2 - Sequencing of Clinical Isolates.'+'\n'

#A usage statement to tell the user how to use the script
if len(sys.argv)!=3:
	print '\n'+'\n'+'\n'+'To use this script, type: python glimmer_orf_extraction.py {input directory [USE THE FULL PATH WITH NO END SLASH]} {output directory [USE THE FULL PATH AND NO END SLASH}'+'\n'
	if len(sys.argv)<3:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>3:
		print 'You added something!'+'\n'
	sys.exit()


#This section loads the files.
files = os.listdir(sys.argv[1])

# #This makes the directory
# if os.path.exists(sys.argv[2])==False:
# 	os.mkdir(sys.argv[2])
# 	print ('Making the directory '+sys.argv[2])

for filename in files:
	if filename.endswith('.fa'):
		print 'Working on '+filename.rstrip('.fa')

		#CHANGING workingdir TO sys.argv[2].IF FAILS, CHANGEBACK ALSO GOES HERE WITH THE MKDIR COMMAND COMMENTED.
		#Making the directory for the file.
		# workingdir='/home/comp/shlab/hschreiber/predicted_orfs/'+filename.rstrip('.fa')+'_glimresults'
		# #os.mkdir(workingdir)

		#Setting the Glimmer command
		glimmercmd='/home/comp/shlab/hschreiber/glimmer3.02/scripts/g3-iterated.csh '+sys.argv[1]+'/'+filename+' '+sys.argv[2]+'/'+filename.rstrip('.fa')
		subprocess.call(glimmercmd, shell=True)

#This section will take the glimmer predict coordinates and extract the ORF in a fasta format
		if os.path.exists(sys.argv[2]+'/'+filename.rstrip('.fa')+'.predict')==True:
			print 'Extracting FASTA ORFs from '+filename
			extractcmd='/home/comp/shlab/hschreiber/glimmer3.02/bin/extract '+sys.argv[1]+'/'+filename+' '+sys.argv[2]+'/'+filename.rstrip('.fa')+'.predict >'+filename.rstrip('.fa')+'_ORFs.fa'
			subprocess.call(extractcmd, shell=True)
			print 'FINISHED! with '+filename
		if os.path.exists(sys.argv[2]+'/'+filename.rstrip('.fa')+'.predict')==False:
			print 'There was an error opening the coordinates file for '+filename
			sys.exit()
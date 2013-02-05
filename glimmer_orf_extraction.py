import sys
import subprocess
import os
import re

print 'This program will call fall in a directory and pass them through Glimmer and multi-extract'+'\n'

#This section 
files = os.listdir('/home/comp/shlab/hschreiber/assembled_genomes')

for filename in files:
	if filename.endswith('.fa'):
		print 'Working on '+filename.rstrip('.fa')

		#Making the directory for the file.
		workingdir='/home/comp/shlab/hschreiber/predicted_orfs/'+filename.rstrip('.fa')+'_glimresults'
		# os.mkdir(workingdir)

		#Setting the Glimmer command
		glimmercmd='/home/comp/shlab/hschreiber/glimmer3.02/sample-run/g3-iterated.csh /home/comp/shlab/hschreiber/assembled_genomes/'+filename+' '+workingdir+'/'+filename.rstrip('.fa')
		subprocess.call(glimmercmd, shell=True)

		if os.path.exists(workingdir+'/'+filename.rstrip('.fa')+'.predict')==True:
			print ('Formatting '+filename.rstrip('.fa')+'.predict')

			#Lets load the input file!
			infile = open (workingdir+'/'+filename.rstrip('.fa')+'.predict')
			if infile == 0:
				print ('There is a problem with the coordinates input file')
				sys.exit()

			outfile = open (workingdir+'/'+filename.rstrip('.fa')+'_formatted.predict','wt')
			if outfile ==0:
				print ('There is a problem with the formatted coordinates output file')
				sys.exit()

			#Lets read the file, line by line for greater tractability of the information
			while True:

				line = infile.readline().rstrip()
				if re.search('>',line):
					header = line.strip('>')
					continue
				
				#When the file runs out of lines, end the while loop
				if line == (''):
					break

				else:
					split = line.split()
					if split != 1:
						combined = split[0] + '     ' + header + '     ' + split[1] + '     ' + split[2]  + '     ' + split[3]  + '     ' + split[4] + '\n'
						outfile.write(combined)
			infile.close()
			outfile.close()

		if os.path.exists(workingdir+'/'+filename.rstrip('.fa')+'_formatted.predict')==True:
			print 'Extracting FASTA ORFs from '+filename
			if os.path.exists(workingdir+'/'+filename.rstrip('.fa')+'_formatted.predict')==True:
				multicmd='/home/comp/shlab/hschreiber/glimmer3.02/bin/multi-extract -w /home/comp/shlab/hschreiber/assembled_genomes/'+filename+' '+workingdir+'/'+filename.rstrip('.fa')+'_formatted.predict >'+workingdir+'/'+filename.rstrip('.fa')+'_ORFs.fa'
				subprocess.call(multicmd, shell=True)
				print 'FINISHED! with '+filename
			else:
				print 'There was an error opening the formatted coordinates file for '+filename
				sys.exit()

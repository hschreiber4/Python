import sys
import subprocess
import os

# This section loads the files.
files = os.listdir(sys.argv[1])
#Starting the loop to look for files.
for filename in files:
	if filename.endswith('.fsa'):
		print 'Working on '+filename
		strain_id=filename.replace('.ps.fsa','')

		#Setting the blastn command
		blastn_cmd='blastn -db '+sys.argv[2]+' -query '+sys.argv[1]+'/'+filename+' -outfmt "6 sseqid evalue pident qcovs qstart qend sstart send sseq" > '+strain_id+'_VFDB_BLAST_results.txt'
		subprocess.call(blastn_cmd, shell=True)
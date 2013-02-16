import sys
import os

if len(sys.argv)!=2:
	print '\n'+'\n'+'\n'+'To use this script, type: python batch_blastn.py {directory of query sequences[USE THE FULL PATH WITH NO END SLASH]} {output directory [USE THE FULL PATH AND NO END SLASH}'+'\n'
	if len(sys.argv)<3:
		print 'You forgot something!'+'\n'
	elif len(sys.argv)>3:
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
				outfile.write(line)
# translate={'SJH_15.fa':'2.1a.fa', 'SJH_16.fa':'2.2r.fa', 'SJH_17.fa':'5.1a.fa', 'SJH_171.fa':'5.2p.fa', 'SJH_18.fa':'5.3r.fa', 'SJH_19.fa':'9.1a.fa', 'SJH_173.fa':'9.2p.fa', 'SJH_20.fa':'9.3r.fa', 'SJH_21.fa':'11.1a.fa', 'SJH_175.fa':'11.2p.fa', 'SJH_22.fa':'11.3r.fa', 'SJH_23.fa':'12.1a.fa', 'SJH_176.fa':'12.2p.fa', 'SJH_24.fa':'12.3r.fa', 'SJH_25.fa':'12.4r.fa', 'SJH_26.fa':'13.1a.fa', 'SJH_179.fa':'13.2p.fa', 'SJH_27.fa':'13.3r.fa', 'SJH_181.fa':'13.4p.fa', 'SJH_28.fa':'13.5r.fa', 'SJH_29.fa':'17.1a.fa', 'SJH_186.fa':'17.2p.fa', 'SJH_30.fa':'17.2r.fa', 'SJH_31.fa':'20.1a.fa', 'SJH_32.fa':'20.2r.fa', 'SJH_33.fa':'20.3r.fa', 'SJH_34.fa':'21.1a.fa', 'SJH_189.fa':'21.2p.fa', 'SJH_35.fa':'21.3r.fa', 'SJH_36.fa':'26.1a.fa', 'SJH_191.fa':'26.2p.fa', 'SJH_37.fa':'26.3r.fa', 'SJH_38.fa':'31.1a.fa', 'SJH_289.fa':'31.2p.fa', 'SJH_39.fa':'31.3r.fa', 'SJH_291.fa':'34.1a.fa', 'SJH_292.fa':'34.2r.fa', 'SJH_294.fa':'35.1a.fa', 'SJH_296.fa':'35.2p.fa', 'SJH_295.fa':'35.3r.fa', 'SJH_298.fa':'41.1a.fa', 'SJH_300.fa':'41.2p.fa', 'SJH_299.fa':'41.3r.fa', 'SJH_303.fa':'41.4p.fa', 'SJH_302.fa':'41.5r.fa', 'SJH_338.fa':'56.1r.fa', 'SJH_341.fa':'56.2r.fa', 'SJH_345.fa':'56.3r'}


# for item in file_list:
# 	if ite
# 	print 'The '+key+' should be '+translate[key]
# 	os.rename(key, translate[key])


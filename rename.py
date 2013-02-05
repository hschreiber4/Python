import sys
import os
import re

# translate={"SJH_15_ORFS.fa":"2.1a.fa", "SJH_16_ORFS.fa":"2.2r.fa", "SJH_17_ORFS.fa":"5.1a.fa", "SJH_171_ORFS.fa":"5.2p.fa", "SJH_18_ORFS.fa":"5.3r.fa", "SJH_19_ORFS.fa":"9.1a.fa", "SJH_173_ORFS.fa":"9.2p.fa", "SJH_20_ORFS.fa":"9.3r.fa", "SJH_21_ORFS.fa":"11.1a.fa", "SJH_175_ORFS.fa":"11.2p.fa", "SJH_22_ORFS.fa":"11.3r.fa", "SJH_23_ORFS.fa":"12.1a.fa", "SJH_176_ORFS.fa":"12.2p.fa", "SJH_24_ORFS.fa":"12.3r.fa", "SJH_25_ORFS.fa":"12.4r.fa", "SJH_26_ORFS.fa":"13.1a.fa", "SJH_179_ORFS.fa":"13.2p.fa", "SJH_27_ORFS.fa":"13.3r.fa", "SJH_181_ORFS.fa":"13.4p.fa", "SJH_28_ORFS.fa":"13.5r.fa", "SJH_29_ORFS.fa":"17.1a.fa", "SJH_186_ORFS.fa":"17.2p.fa", "SJH_30_ORFS.fa":"17.2r.fa", "SJH_31_ORFS.fa":"20.1a.fa", "SJH_32_ORFS.fa":"20.2r.fa", "SJH_33_ORFS.fa":"20.3r.fa", "SJH_34_ORFS.fa":"21.1a.fa", "SJH_189_ORFS.fa":"21.2p.fa", "SJH_35_ORFS.fa":"21.3r.fa", "SJH_36_ORFS.fa":"26.1a.fa", "SJH_191_ORFS.fa":"26.2p.fa", "SJH_37_ORFS.fa":"26.3r.fa", "SJH_38_ORFS.fa":"31.1a.fa", "SJH_289_ORFS.fa":"31.2p.fa", "SJH_39_ORFS.fa":"31.3r.fa", "SJH_291_ORFS.fa":"34.1a.fa", "SJH_292_ORFS.fa":"34.2r.fa", "SJH_294_ORFS.fa":"35.1a.fa", "SJH_296_ORFS.fa":"35.2p.fa", "SJH_295_ORFS.fa":"35.3r.fa", "SJH_298_ORFS.fa":"41.1a.fa", "SJH_300_ORFS.fa":"41.2p.fa", "SJH_299_ORFS.fa":"41.3r.fa", "SJH_303_ORFS.fa":"41.4p.fa", "SJH_302_ORFS.fa":"41.5r.fa", "SJH_338_ORFS.fa":"56.1r.fa", "SJH_341_ORFS.fa":"56.2r.fa", "SJH_345_ORFS.fa":"56.3r"}

os.rename('./SJH_15_ORFS','./2.1a.fa')

# files = os.listdir('/Users/hschreiber4/Dropbox/Hultgren_Lab_Research/predicted_orfs')


# for filename in files:
# 	if filename.endswith('SJH_15_ORFS.fa'):
# 		print 'Working on '+filename.rstrip('.fa')
# 		# newname = translate[filename]
# 		newname='2.1a.fa'
# 		os.rename(filename,newname)

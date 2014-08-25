#!/usr/bin/env python

import scipy as sp
import scipy.stats
import sys
import collections

if len(sys.argv)!=5:
	print "Usage [SCRIPT NAME] [PROTEIN HITS FILE 1] [PROTEIN HITS FILE 2] [NUMBER OF GENOMES IN FILE 1] [NUMBER OF GENOMES IN FILE 2]"
	sys.exit()

#This def turns the protein hits files into dict that can be used for fisher's exact test
def makedict(filename):
	d={}
	for line in open(filename):
		lineparts=line.strip('\n').split('\t')
		d[lineparts[0]]=int(lineparts[1])
	return d

#This section prints the fisher exact test results
def dictprint(d):
	od=collections.OrderedDict(sorted(d.items()))
	for k, v in od.iteritems():
		print "{:s}\t{:.3g}\t{:.3g}".format(k, v[0], v[1])

UPEC=makedict(sys.argv[1])
NONUPEC=makedict(sys.argv[2])
over={}
under={}
notsig={}

#This section will check for non-zero values in either group of protein hits, load dictionaries for over, under, and not significantly different presence of proteins between the groups.  This section also prints the percentage of genomes containing the proteins in the different groups.
print "Name	UPEC	NONUPEC"
for key in UPEC:
	if UPEC[key]>0 or NONUPEC[key]>0:
		print "{:s}\t{:.3f}\t{:.3f}".format(key, UPEC[key]/float(sys.argv[3]), NONUPEC[key]/float(sys.argv[4]))
		oddsratio, pvalue = sp.stats.fisher_exact([[UPEC[key],NONUPEC[key]],[(int(sys.argv[3])-UPEC[key]),(int(sys.argv[4])-NONUPEC[key])]])
		if pvalue<0.05:
			if oddsratio>1:
				over[key]=(oddsratio, pvalue)
			if oddsratio<1:
				under[key]=(oddsratio, pvalue)
		else:
			notsig[key]=(oddsratio, pvalue)

print "\nOver-represented in UPEC\tOdds-ratio\tpvalue"
dictprint(over)
print "\nUnder-represented in UPEC\tOdds-ratio\tpvalue"
dictprint(under)
print "\nNo significant different in UPEC and NONUPEC\tOdds-ratio\tpvalue"
dictprint(notsig)
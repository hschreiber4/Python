
# read lines and split to get strain name and cluster number. Take cluster number and make a list of strains contianing the strain name. Then turn list into a set and compare the set against a set of all strains made from a list.
# Will then compare list in set format to identify intersection between two sets. If all items in the set intersect, then I will add the node to a collection of core genes. If the strain is in >1 strain, then it will be auxilliary, and if the gene cluster is unique, then I will add it to unique strains.

#Accomplished using set command to turn a dict value called by a key 

#!/usr/bin/env python

import sys as s
from collections import defaultdict

names=set()
clusters=[]
strains=[]
core=[]
cored=defaultdict(list)
unique=[]
uniqued=defaultdict(list)
aux=[]
auxd=defaultdict(list)
d=defaultdict(list)


for line in open(s.argv[2]):
	names.add(line.rstrip('\n'))

for line in open(s.argv[1]):
	clusters.append(line.split('\t')[0])
	strains.append(line.split('\t')[1])

for x,y in zip(clusters,strains):
	for name in names:
		if name in y:
			d[x].append(y)

for k in d:
	s=set(d[k])
	if len(names.difference(s))==0:
		core.append(k)
		for t in s:
			cored[t].append(k)
	if len(names.intersection(s))==1:
		unique.append(k)
		for t in s:
			uniqued[t].append(k)
	if len(names.intersection(s))>1 and len(names.intersection(s))<len(names):
		aux.append(k)
		for t in s:
			auxd[t].append(k)
	
print 'Core: '+str(len(core))
print 'Aux: '+str(len(aux))
print 'Unique: '+str(len(unique))
print 'Total: '+str(len(d))


print('Strain\tCore\tAux\tUnique')
for key in cored:
	print("{0}\t{1}\t{2}\t{3}".format(key,len(cored[key]),len(auxd[key]),len(uniqued[key])))
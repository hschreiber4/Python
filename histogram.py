#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys

UPECdata=[]
NONUPECdata=[]
ALLdata=[]

def makelist(filename):
	d=[]
	for line in open (filename):
		line=line.strip('\n')
		lineparts=line.split('\t')
		d.append(int(lineparts[1]))
		ALLdata.append(int(lineparts[1]))
	return d

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom')

UPECdata=makelist(sys.argv[1])
NONUPECdata=makelist(sys.argv[2])

x=[]
UPECy=[]
NONUPECy=[]

for i in range(min(ALLdata),max(ALLdata)+1):
 	x.append(i)
	UPECy.append(UPECdata.count(i))
	NONUPECy.append(NONUPECdata.count(i))

N=1+max(ALLdata)-min(ALLdata)

index=np.arange(N)
width=0.35

fig=plt.figure()
ax=fig.add_subplot(111)

UPECrects=ax.bar(index, UPECy, width, align='center', color='red')
NONUPECrects=ax.bar(index+width, NONUPECy, width, align='center', color='blue')
ax.set_ylabel('Frequency')
ax.set_xlabel('Number of Usher Genes')
ax.set_yticks(range(0,N+5,5))
ax.set_xticks(index+width)
ax.set_xticklabels(range(min(ALLdata),max(ALLdata)+1))
ax.legend((UPECrects[0],NONUPECrects[0]), ("Urine Isolates", "Other Isolates"))

autolabel(UPECrects)
autolabel(NONUPECrects)

plt.show()
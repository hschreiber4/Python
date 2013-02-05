# Molly Gibson
# Helper code for translation, etc.
print ('Translating time')

import re
import sys

#A usage statement to tell the user how to use the script
if len(sys.argv)!=3:
    print '\n'+'\n'+'\n'+'To use this script, type: python modified_translate.py {input nucleotide file} {output amino acid file}'+'\n'
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

#The output file.
outfile = open (sys.argv[2],'wt')
if outfile ==0:
    print ('There is a problem with the output file')
    sys.exit()





#This section is the heart of the machine.  It performs the translate function.
codon_map = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
             "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
             "TAT":"Y", "TAC":"Y", "TAA":"*", "TAG":"*",
             "TGT":"C", "TGC":"C", "TGA":"*", "TGG":"W",
             "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
             "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
             "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
             "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
             "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
             "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
             "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
             "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
             "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
             "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
             "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
             "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def translate(DNA):
    letters = []
    start = 0
    while start+2 < len(DNA):
        codon = DNA[start:start+3]
        letters.append(codon_map[codon])
        start+=3
    return ''.join(letters)

def reverseComplement(s):
    s = s[::-1] 
    s = complement(s) 
    return s    

def complement(s): 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    letters = list(s) 
    letters = [basecomplement[base] for base in letters] 
    return ''.join(letters)

#Defining variables for later use.
headers=[]
sequences=[]
separatedsequence=''


#Lets read the file, line by line for greater tractability of the information
while True:
    line = infile.readline().rstrip().strip('\n').strip('\r')

    #When the file runs out of lines, end the while loop
    if line == (''):
        sequences.append(separatedsequence)
        break
#This finds the headders and appends the sequence to the list of other sequences.
    if re.search('>',line):
        headers.append(line)
        sequences.append(separatedsequence)
        separatedsequence=''
    
    else:
        separatedsequence = separatedsequence + line

i=0
trans_sequences=[]
while i < len(headers):
    trans_sequences=translate(sequences[i+1])
    outfile.write(headers[i]+'\n')
    outfile.write(translate(sequences[i+1])+'\n')
#Let's add one to our counting variable.
    i+=1



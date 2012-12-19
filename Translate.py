# Molly Gibson
# Helper code for translation, etc.

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

#!/usr/bin/env python

from Bio import SeqIO
import sys as s

gene_list = ["UTI89_C3219", "UTI89_C4551", "UTI89_C4550", "UTI89_C4549", "UTI89_C4548", "UTI89_C3862", "UTI89_C4860", "UTI89_C4857", "UTI89_C4856", "UTI89_C4855", "UTI89_C4854", "UTI89_C4853", "UTI89_C0965", "UTI89_C3327", "UTI89_C3325", "UTI89_C0133", "UTI89_C0694"]

for seq_record in SeqIO.parse("sequence.txt", "fasta"):
	for gene in gene_list:
		if gene in seq_record.description:
			print ">{:s}".format(seq_record.description)
			print seq_record.seq
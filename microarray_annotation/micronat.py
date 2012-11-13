#Here are all my imports
import re
import sys

#This function takes a search term given in the elif search blocks and
#isolates the relevent data from the line.
def isolate(search_term, search_line):
	split_term = search_line.split(search_term)
	formatted_term = split_term[1].replace('\"','').replace('\n','')
	return formatted_term

#Opening a writable file
out_file=open('output.txt','wt')

#Hard coding the input file for easier coding to start with
for line in open('short_file.txt'):

#Now the searches begin
	if re.search('CDS', line) and re.search('..', line):
#Finding the gene location and then isolating the numbers
		gene_loc = line.split('CDS')
		formatted_gene_loc = gene_loc[1].replace(' ','').rstrip('\n')
		gene_boundaries = formatted_gene_loc.split('..')
		gene_size=int(gene_boundaries[1])-int(gene_boundaries[0])
		out_file.write(str(gene_boundaries[0])+'\t'+str(gene_boundaries[1])+'\t'+str(gene_size)+'\t')

		for subline in open('short_file.txt'):

#Finding the gene name and isolating it
			if re.search('/gene',subline):
				gene_tag = isolate('/gene=',subline)
				print gene_tag

#Finding the locus tag and isolating it
			elif re.search('/locus_tag',subline):
				locus_tag = isolate('tag=', subline)

#Finding the function and isolating it
			elif re.search('/function', subline):
				function_tag = isolate('function=', subline)

#Finding the protein id and isolating it
			elif re.search('protein_id=',subline):
				protein_tag = isolate('_id=', subline)

#Finding the GI and isolating it
			elif re.search('"GI:',subline):
				GI_tag = isolate('xref=',subline)




# #Finding the note and isolating it
# 	elif re.search('/note=',line):
# 		note_tag = isolate('/note=',line)
# 		while True:
# 			note_lines=line.read()
# 			if re.search('/codon_start',note_lines):
# 				break
# 			else:
# 				print note_lines
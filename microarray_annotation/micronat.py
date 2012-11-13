#Here are all my imports
import re
import sys

#This function takes a search term given in the elif search blocks and
#isolates the relevent data from the line.
def isolate(search_term, search_line):
	split_term = search_line.split(search_term)
	formatted_term = split_term[1].replace('\"','').replace('\n','')
	return formatted_term

#Hard coding the input file for easier coding to start with

for line in open('short_file.txt'):

#Now the searches begin
#Finding the gene location and then isolating the numbers
	if re.search('gene', line) and re.search('\.\.', line):
		gene_loc = line.split('gene')
		formatted_gene_loc = gene_loc[1].replace(' ','').rstrip('\n')
		gene_boundaries = formatted_gene_loc.split('..')
		gene_size=int(gene_boundaries[1])-int(gene_boundaries[0])

#Finding the gene name and isolating it
	elif re.search('/gene',line):
		gene_tag = isolate('/gene=',line)

#Finding the locus tag and isolating it
	elif re.search('/locus_tag',line):
		locus_tag = isolate('tag=', line)

#Finding the function and isolating it
	elif re.search('/function', line):
		function_tag = isolate('function=', line)

#Finding the protein id and isolating it
	elif re.search('protein_id=',line):
		protein_tag = isolate('_id=', line)

#Finding the GI and isolating it
	elif re.search('"GI:',line):
		GI_tag = isolate('xref=',line)

#Making a print statement
	# print '{gene_start}\t{gene_end}\t{gene_length}\t{gene_name}\t{locus_name}\t{function_name}\t{protein_name}\t{GI_name}'.format(gene_start=gene_boundaries[0], gene_end=gene_boundaries[1], gene_length=gene_size, gene_name=gene_size, locus_name=locus_tag, function_name=function_tag, protein_name=protein_tag, GI_name=GI_tag)


# #Finding the note and isolating it
# 	elif re.search('/note=',line):
# 		note_tag = isolate('/note=',line)
# 		while True:
# 			note_lines=line.read()
# 			if re.search('/codon_start',note_lines):
# 				break
# 			else:
# 				print note_lines
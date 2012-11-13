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
for line in open('UTI89_genome.txt'):

#Now the searches begin
#Finding the gene location and then isolating the numbers
	if re.search('gene', line) and re.search('\.\.', line):
		if re.search('complement',line):
			line.replace('complement','').replace('\(','').replace('\)','')
		
		else:
			gene_loc = line.split('gene')
			formatted_gene_loc = gene_loc[1].replace(' ','').rstrip('\n')
			gene_boundaries = formatted_gene_loc.split('..')
			gene_size=int(gene_boundaries[1])-int(gene_boundaries[0])
			out_file.write(str(gene_boundaries[0])+'\t'+str(gene_boundaries[1])+'\t'+str(gene_size)+'\t')

#Finding the gene name and isolating it
	elif re.search('/gene=',line):
		gene_tag = isolate('/gene=',line)
		out_file.write(gene_tag+'\t')

#Finding the locus tag and isolating it
	elif re.search('/locus_tag',line):
		locus_tag = isolate('tag=', line)
		out_file.write(locus_tag+'\t')

#Finding the function and isolating it
	elif re.search('/function', line):
		function_tag = isolate('function=', line)
		out_file.write(function_tag+'\t')

#Finding the protein id and isolating it
	elif re.search('protein_id=',line):
		protein_tag = isolate('_id=', line)
		out_file.write(protein_tag+'\t')

#Finding the GI and isolating it
	elif re.search('"GI:',line):
		GI_tag = isolate('xref=',line)
		out_file.write(GI_tag+'\n')

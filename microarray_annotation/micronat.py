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

#Finding the gene name and isolating it
	elif re.search('/gene',line):
		gene_name = isolate('/gene=',line)

#Finding the locus tag and isolating it
	elif re.search('/locus_tag',line):
		locus_tag = isolate('tag=', line)

#Finding the function and isolating it
	elif re.search('/function', line):
		function_tag = isolate('function=', line)

#Finding the protein id and isolating it
	elif re.search('protein_id=',line):
		protein_name = isolate('_id=', line)

#Finding the GI and isolating it
	elif re.search('"GI:',line):
		GI_tag = isolate('xref=',line)

#Finding the note and isolating it
	elif re.search('/note=',line):
		note_tag = isolate('/note=',line)
		while True:
			note_lines=line.readline()
			if re.match([a-z],note_lines):
				print note_lines
			elif re.match()

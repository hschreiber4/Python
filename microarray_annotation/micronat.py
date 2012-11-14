#This program is designed to reformat a Genbank file from a single column
#format into a tab-delimited format that is readable using Excel.  Much of the
#information in the Genbank file is not useful for most purposes, and, as a
#result, has been filtered out of the reformatting.  Only the gene start,
#gene, end, gene size, locus name, gene name, product description, functional
#annotations, context annotations, GI number and protein ID have been
#included.  This script was written using the E. coli UTI89 genome as a
#template, but it should be applicable to all bacterial genomes.

# If you have questions, comments, or advise, please email henry.l.schreiber+work@gmail.com

#Here are all my imports
import re
import sys

#This function takes a search term given in the elif search blocks and
#isolates the relevent data from the line.
def isolate(search_term, search_line):
	split_term = search_line.split(search_term)
	formatted_term = split_term[1].replace('\"','').replace('\n','')
	return formatted_term

#Opening the input file
genfile = open(sys.argv[1])

#Opening a writable file
out_file=open(sys.argv[2],'wt')

#This section sets the initial variables as placeholders.
gene_boundaries = [1,2]
gene_size=2
gene_tag='no_gene_name_annotation'
locus_tag='no_locus_annotation'
product_tag='no_product_annotation'
function_tag='no_function_annotation'
note_tag='no_note_annotation'
protein_tag='no_protein_ID'
GI_tag='no_GI_number'

#Starting the loop with this version in order to have better access to following lines of code, rather than using a for .. in loop.
while True:

#Beginning to read the lines
	line = genfile.readline()

#Now the searches begin
#Finding the gene location and then isolating the numbers
	if re.search('gene', line) and re.search('\.\.', line):

#This writes all of the varaibles to the proper file.  It will include a useless line at the beginning, but it is functional.
		out_file.write(str(gene_boundaries[0])+'\t'+str(gene_boundaries[1])+'\t'+str(gene_size)+'\t'+gene_tag+'\t'+locus_tag+'\t'+product_tag+'\t'+function_tag+'\t'+note_tag+'\t'+protein_tag+'\t'+GI_tag+'\n')

#This block resets all of the variables.  These are nonsense placeholders.
		gene_boundaries = [1,2]
		gene_size=2
		gene_tag='no_gene_name_annotation'
		locus_tag='no_locus_annotation'
		product_tag='no_product_annotation'
		function_tag='no_function_annotation'
		note_tag='no_note_annotation'
		protein_tag='no_protein_ID'
		GI_tag='no_GI_number'

#These two blocks will reformat the gene line depending on the composition of
#the line.  Necessary to prevent errors in lines that contain the phrase
#'complement'
		if re.search('complement',line):
			line.split('complement')
			gene_loc = line.split('gene')
			formatted_gene_loc = gene_loc[1].strip().strip('complement').strip('\(').strip('\)').rstrip('\n')
			gene_boundaries = formatted_gene_loc.split('..')
			gene_size=int(gene_boundaries[1])-int(gene_boundaries[0])
		
		else:
			gene_loc = line.split('gene')
			formatted_gene_loc = gene_loc[1].replace(' ','').rstrip('\n')
			gene_boundaries = formatted_gene_loc.split('..')
			gene_size=int(gene_boundaries[1])-int(gene_boundaries[0])

#Finding the gene name and isolating it
	elif re.search('/gene=',line):
		gene_tag = isolate('/gene=',line)

#Finding the locus tag and isolating it
	elif re.search('/locus_tag=',line):
		locus_tag = isolate('tag=', line)

#Finding the protein product
	elif re.search('/product=',line):
		product_tag = isolate('product=', line)

#Finding the function and isolating it.  This section also sets the note
#entry.  The while while loop is necessary to get the multiple lines of both
#the function and note lines, if there are multiple lines in each entry.
	elif re.search('/function=', line):
		function_tag = isolate('function=', line)
		while True:
			fun_line=genfile.readline()
			if re.search('/note=', fun_line):
				note_tag = isolate('note=', fun_line)
				while True:
					note_line=genfile.readline()
					if re.search('_start', note_line):
						break
#For some reason, I could not get the additional lines to append to the end of
#the note annotation without using the gimmick.  Please advise if you have a
#better option.
					else:
						split_note_line=note_line.split()
						for thing in split_note_line:
							note_tag=note_tag+' '+thing
				break
			elif re.search('_start',fun_line):
				break
#As above, I used this gimmick to append the extra function lines, if any, to
#the output.  I am unsure as to the reason appending complete lines proved
#difficult.
			else:
				split_fun_line = fun_line.split()
				for word in split_fun_line:
					function_tag=function_tag+' '+word

#Finding the protein id and isolating it
	elif re.search('protein_id=',line):
		protein_tag = isolate('_id=', line)


#Finding the GI and isolating it
	elif re.search('"GI:',line):
		GI_tag = isolate('xref=',line)


#When the file runs out of lines, end the while loop
	elif line == (''):
		break

#One last print outside of the while loop in order to get the last line of text
out_file.write(str(gene_boundaries[0])+'\t'+str(gene_boundaries[1])+'\t'+str(gene_size)+'\t'+gene_tag+'\t'+locus_tag+'\t'+product_tag+'\t'+function_tag+'\t'+note_tag+'\t'+protein_tag+'\t'+GI_tag+'\n')

#This is the function that will take individual header and sequence and format them into FASTA format 
def fasta_format(header, sequence):     
	fasta_string ='>{the_header}\n{the_sequence}\n\n'.format(the_header=header,the_sequence=sequence)
	return fasta_string

#This section loads a list with a number of header lines from a file after splitting them along on the new line function
headers_file = open('headers.txt')
all_the_headers = headers_file.read().split('\n')
headers_file.close()
print 'The headers are:'
print all_the_headers

#This section loads a list with a number of sequence lines from a file. The list is split on new line ca
sequences_file = open('sequences.txt')
all_the_sequences = sequences_file.read().split('\n')
sequences_file.close()
print 'The sequences are: '
print all_the_sequences

#This section opens a writable file that will be filled with the headers and sequences
output_file = open('output.txt','wt')


#This section writes each new header and sequence together into the open output file.
for x in range(len(all_the_headers)):
	output_file.write(fasta_format(all_the_headers[x], all_the_sequences[x]))
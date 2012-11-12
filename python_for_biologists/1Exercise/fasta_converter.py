print ('This is exercise2')

header_file =  open ('headers.txt')
header = header_file.read()

sequence_file = open ('sequences.txt')
sequence = sequence_file.read()

print 'The headers are' + header
print 'The sequences are' +sequence
# output_file = open ('converted_fasta.txt', 'wt')
# output_file.write('>' + first_name + '\n' + last_name)
# output_file.close()

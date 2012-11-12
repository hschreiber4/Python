print ('This is exercise2')

header_file =  open ('header.txt')

first_name = first_name_file.read()

last_name_file = open ('lastname.txt')
last_name = last_name_file.read()

output_file = open ('fullname.txt', 'wt')
output_file.write('>' + first_name + '\n' + last_name)
output_file.close()

print (first_name + '\n')
print (str(len(last_name)))

lowercase = last_name.lower()

print (lowercase)

lowercase = lowercase.replace('t','u')

print (lowercase)
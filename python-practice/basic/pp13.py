import csv

with open('example.csv') as file:
    file_reader = csv.reader(file)
    content = list(file_reader)
    # print(content[0:2])
    # print(file_reader)
#     for row in file_reader:
#         print('Row: ' + str(file_reader.line_num) + str(row))

# output_file = open('output.csv', 'a', newline='')
# output_writer = csv.writer(output_file)
# output_writer.writerow(['16/11/2021', 'Tuesday', 'Learning Python Part-1'])
# output_writer.writerow(['17/11/2021', 'Wednesday', 'Learning Python Part-2'])
# output_writer.writerow(['18/11/2021', 'Thursday', 'Learning Python Part-3'])
# output_writer.writerow(['19/11/2021', 'Friday', 'Learning Python Part-4'])
# output_file.close()
output = open('output.csv')
output_reader = csv.reader(output)
for row in output_reader:
    print(str(output_reader.line_num) + ': '+ str(row))

import os
import sys
import operator

input_dir = '/home/detectivelyw/Documents/projects/tracks/linuxkit-auto-experiment/gcov-parsed-data/'  

container_name = sys.argv[1]
num_iterations = sys.argv[2]

gcov_data_sets = dict()
total_set = set()

array = [[]]

output_dir = '/home/detectivelyw/Documents/projects/tracks/linuxkit-auto-experiment/added-new-lines/' + container_name + '-' + num_iterations   
try:  
    os.mkdir(output_dir)
except OSError:  
    print ("Creation of the directory %s failed" % output_dir)
else:  
    print ("Successfully created the directory %s " % output_dir)

for i in range(1, int(num_iterations)+1):
  inputfile_set = set()
  input_file_name = input_dir + "gcov-data-" + container_name + "-parsed-" + str(i) + ".txt"
  with open(input_file_name) as input_file:  
    line = input_file.readline()
    while line:
      inputfile_set.add(line)    
      line = input_file.readline()
  input_file.close()
  gcov_data_sets[str(i)] = inputfile_set
  total_set = total_set | inputfile_set
  item = []
  item.append(i)
  item.append(len(inputfile_set))
  array.append(item)

del array[0]

for j in range(1, int(num_iterations)+1):
  others_set = set()
  for k in range(1, int(num_iterations)+1):
    if (k != j):
      others_set = others_set | gcov_data_sets[str(k)]
  unique_set = set()
  unique_set = total_set - others_set
  print(str(j) + ": " + str(len(unique_set)))    
  item2 = []
  item2.append(j)
  item2.append(len(unique_set))
  for item3 in array:
    if item2[0] == item3[0]:
      item3.append(item2[1])

array.sort(key = operator.itemgetter(2, 1))

total_num_lines = len(total_set)
current_union_set = set()
previous_union_set = set()

counter = 0
for item4 in array:
  counter += 1

  output_file_name = output_dir + '/added_new_lines-output-' + container_name + '-' + str(counter) + '.txt'
  output_file = open(output_file_name, 'w+')

  current_union_set = previous_union_set | gcov_data_sets[str(item4[0])]
  newlines_set = set()
  newlines_set = current_union_set - previous_union_set
  previous_union_set = current_union_set
  
  for line in newlines_set:
    output_file.write(line)
  output_file.close() 


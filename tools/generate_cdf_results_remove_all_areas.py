import sys
import operator

input_dir = '/home/detectivelyw/Documents/projects/tracks/linuxkit-auto-experiment/gcov-parsed-data/'  

container_name = sys.argv[1]
num_iterations = sys.argv[2]

gcov_data_sets = dict()
total_set = set()
total_removed_set = set()

array = [[]]

common_kernel_areas_set = set()
common_kernel_areas_filename = "overlaps-10-containers.txt"
with open(common_kernel_areas_filename) as common_kernel_areas_file:  
  kernel_line = common_kernel_areas_file.readline()
  while kernel_line:
    if kernel_line != "\n":  
      common_kernel_areas_set.add(kernel_line)    
    kernel_line = common_kernel_areas_file.readline()
common_kernel_areas_file.close()

for i in range(1, int(num_iterations)+1):
  inputfile_set = set()
  input_file_name = input_dir + "gcov-data-" + container_name + "-parsed-" + str(i) + ".txt"
  with open(input_file_name) as input_file:  
    line = input_file.readline()
    while line:
      inputfile_set.add(line)    
      line = input_file.readline()
  input_file.close()
  gcov_data_sets[str(i)] = inputfile_set - common_kernel_areas_set
  total_set = total_set | inputfile_set
  total_removed_set = total_removed_set | gcov_data_sets[str(i)]
  item = []
  item.append(i)
  item.append(len(gcov_data_sets[str(i)]))
  array.append(item)

del array[0]

for j in range(1, int(num_iterations)+1):
  others_set = set()
  for k in range(1, int(num_iterations)+1):
    if (k != j):
      others_set = others_set | gcov_data_sets[str(k)]
  unique_set = set()
  unique_set = total_removed_set - others_set
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

output_file_name = 'cdf-removed-output-' + container_name + num_iterations + '.txt'
output_file = open(output_file_name, 'w+')
output_file.write("iterations " + container_name + "\n")

counter = 0
for item4 in array:
  counter += 1
  current_union_set = current_union_set | gcov_data_sets[str(item4[0])]
  current_num_lines = len(current_union_set)
  current_ratio = float(current_num_lines) / float(total_num_lines)
  if ((counter % 10) == 0):
    output_file.write(str(counter) + " " + str(current_ratio) + "\n")
  else:
    output_file.write(". " + str(current_ratio) + "\n")
output_file.close() 


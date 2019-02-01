import sys
import operator

input_dir = '/home/detectivelyw/Documents/projects/tracks/linuxkit-auto-experiment/added-new-lines/'  

threshold = 20

containers = ["nginx", "memcached", "redis", "mongo", "mysql", "traefik", "python", "node", "php", "openjdk"]
arrays = [[]]

for container in containers: 
  array = [[]]
  for i in range(1, 101, 1):
    input_file_name = input_dir + container + "-100/" + "added_new_lines-output-" + container + "-" + str(i) + ".txt"
    tmp_set = set()
    with open(input_file_name) as input_file:  
      line = input_file.readline()
      while line:
        tmp_set.add(line)    
        line = input_file.readline()
    input_file.close()
    if ((len(tmp_set) >= threshold) and (i != 1)): 
      # print input_file_name + ": " + str(len(tmp_set))
      item = []
      item.append(i)
      item.append(tmp_set)
      array.append(item)
  del array[0]
  item2 = []
  item2.append(container)
  item2.append(array)
  arrays.append(item2)

del arrays[0]
#print arrays
for item in arrays: 
  # print item[0]
  for item2 in item[1]:
    # print "*** analyzing " + str(item2[0]) + " " + str(len(item2[1])) + " ***"
    for item_cmp in arrays:
      if item_cmp != item:  
        for item_cmp2 in item_cmp[1]:
          overlap_set = set()
          overlap_set = item2[1] & item_cmp2[1]
          if len(overlap_set) != 0:
            # print "overlap between " + str(item[0]) + "-run-" + str(item2[0]) + " & " + str(item_cmp[0]) +"-run-" + str(item_cmp2[0]) + " = " + str(len(overlap_set))
            for line in overlap_set:
              print line
    # print "*** analyzing done!" 



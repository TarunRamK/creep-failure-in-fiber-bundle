import os
import csv
import numpy as np

def g_index(trimmed_array):
    trimmed_array.sort()
    cu_array = [sum(trimmed_array[0:i+1]) for i in range(0, len(trimmed_array))]
    max_val = max(cu_array)    
    lor_array = [i/max_val for i in cu_array]

    area = 0
    dt = 1/(len(lor_array)+1)
    for i in lor_array:
        area = area + (i*dt)
    
    tot_area = 0.5
    g_ind = (tot_area - area)/ tot_area
    return g_ind

def k_index(trimmed_array):
    trimmed_array.sort()
    cu_array = [sum(trimmed_array[0:i+1]) for i in range(0, len(trimmed_array))]
    lor_array = [i/max(cu_array) for i in cu_array]

    delta = 1/len(lor_array)
    k=0
    index = 0
    while(k<=1):
        if (1-k) - lor_array[index] <= 0:
          return k
        k = k + delta
        index = index+1
        if k >= 1:
          print("Cound not find k index")
          break



def is_crossing(li):
    g_val = g_index(li)
    k_val = k_index(li)
    diff = g_val - k_val
    if diff>=0:
        return [1, diff, g_val, k_val]
    if diff<=0:
        return [0, diff, g_val, k_val]

    
    



dir_name = 's0.3/Files/Time Rate Data/'
li = os.listdir(dir_name)
print(li)
output_file = open("phase_results/s.3.txt","a")


out_li = []
f_no=1
for f_name in li:
    array1 = []
    file_name = dir_name + f_name
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            array1.append(int(row[1]))
        result = is_crossing(array1)
        output_file.write(str(result[0]) +" "+ str(result[1]) +" "+ str(result[2]) +" "+ str(result[3]) +"\n")
output_file.close()
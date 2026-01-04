import math
import time
import itertools
from array import array
import ast

num_vals = 1001
master_array = [0]*num_vals
individual_arrays = [[],[],[],[],[]]
for index in range(5):
    individual_arrays[index] = [0]*num_vals

folder_location = '/home/nhemleben/Python_Scripts/Countdown_Solver/'
for num_large in [0,1,2,3,4]:
    file_name = 'dynamic_results_num_large_' +str(num_large) + '.txt'
    
    with open(folder_location + file_name, 'r') as f:
        for line in f:
            #value, counts = map(array, line.split("),["))

            # Split "(tuple),[list]"
            _, counts_str = line.split("],", 1) if False else line.split("),", 1)
            # Parse the list safely
            counts = ast.literal_eval(counts_str.strip())



            for index in range(num_vals):
                individual_arrays[num_large][index] += counts[index]

    for index in range(num_vals):
        master_array[index] += individual_arrays[num_large][index]

    print(num_large)

print( individual_arrays)
print( master_array)


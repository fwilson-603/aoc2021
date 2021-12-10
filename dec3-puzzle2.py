# Advent of Code 2021; Dec 3, second puzzle

## SUCCESSFULLY SUBMITTED

# import needed material
import statistics
import collections
from collections import Counter

# load input file
input = open("dec3-input.txt", "r")

# store input file in an array
binary_values = []
for x in input:
    binary_values.append(x)
    
# calculate length of binary input items
test_item = str(binary_values[0])
length_of_items = len(test_item)

# function for finding oxygen generator rating
def oxy_gen_calculate():
    global oxygen_values
    oxygen_values = binary_values
    for x in range(0, (length_of_items)-1):
        stored_values = []
        temp_oxygen_values = []
        for i in oxygen_values:
            number = i[x:x+1]
            stored_values.append(int(number))
        frequency = Counter(stored_values).most_common()
        if frequency[0][1] == frequency[1][1]:
            target = 1
        elif frequency[0][0] == 1:
            target = 1
        elif frequency[0][0] == 0:
            target = 0
        for y in oxygen_values:
            if int(y[x]) == target:
                temp_oxygen_values.append(y)
        oxygen_values = temp_oxygen_values
        if len(oxygen_values) == 1:
            break

# function for finding c02 scrubber rating
def c02_scrubb_calculate():
    global c02_values
    c02_values = binary_values
    for x in range(0, (length_of_items)-1):
        stored_values = []
        temp_c02_values = []
        for i in c02_values:
            number = i[x:x+1]
            stored_values.append(int(number))
        frequency = Counter(stored_values).most_common()
        if frequency[0][1] == frequency[1][1]:
            target = 0
        elif frequency[0][0] == 1:
            target = 0
        elif frequency[0][0] == 0:
            target = 1
        for y in c02_values:
            if int(y[x]) == target:
                temp_c02_values.append(y)
        c02_values = temp_c02_values
        if len(c02_values) == 1:
            break

# run function to find oxygen generator and c02 scrubber ratings
oxy_gen_calculate()
c02_scrubb_calculate()

# turn the strings into integers of the right length
oxygen_gen_rating = oxygen_values[0][:12]
c02_scrubb_rating = c02_values[0][:12]

# function for converting binary to decimal notation
def convert_to_dec(item):
    return int(item, 2)

# run function to convert to decimal
oxygen_gen_dec = convert_to_dec(oxygen_gen_rating)
c02_scrubb_dec = convert_to_dec(c02_scrubb_rating)

# find life support rating
life_support_rating = oxygen_gen_dec * c02_scrubb_dec
print(life_support_rating)

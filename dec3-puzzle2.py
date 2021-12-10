# Advent of Code 2021; Dec 3, first puzzle

## DOESN'T WORK YET

## start with the full list of binary numbers
## consider the first bit of those numbers
## keep only the numbers selected by the bit criteria
## if you have only one number left, stop
## if there is more than one number, repeat the process

## bit criteria: for oxygen, most common value in the position
## keep only numbers with that bit in that position
## if 0 and 1 are equally common, keep values with 1

## c02 scrubber rating, keep only least common value
## if 0 and 1 are equally common, keep 0

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

# start with the full list of binary numbers
# consider just the first bit of those numbers

# keep only numbers selected by the bit criteria for the 
# type of rating value for which you are searching
# if you have only one number left, stop
# otherwise, repeat the process, considering
# the next bit to the right

# for oxygen generator rating
# most common value in the current bit position
# keep only numbers with that bit in that position
# if 0 and 1 are equally common, keep values with a 0 in the position

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

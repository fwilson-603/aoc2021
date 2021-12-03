# Advent of Code 2021; Dec 3, first puzzle

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

# establish variables for gamma and epsilon rate
gamma_rate_bin = []
epsilon_rate_bin = []
gamma_rate_string = ""
epsilon_rate_string = ""

# function to find the most and least common items
def binary_eval(x, report):
    stored_values = []
    for i in report:
        number = i[x:x+1]
        stored_values.append(int(number))
    frequency = Counter(stored_values).most_common()
    high_freq = frequency[0]
    low_freq = frequency[-1]
    gamma_rate_bin.append(high_freq)
    epsilon_rate_bin.append(low_freq)
    
# calculate length of binary input items
test_item = str(binary_values[0])
length_of_items = len(test_item)
    
# loop through a range defined by the length of the binary
# input, and run function binary_eval() on each one
for y in range(0, (length_of_items)-1): ## check range
    binary_eval(y, binary_values)

# translate the lists into strings
for z in gamma_rate_bin:
    gamma_rate_string += str(z[0])
for z in epsilon_rate_bin:
    epsilon_rate_string += str(z[0])

# function for converting binary to decimal notation
def convert_to_dec(item):
    return int(item, 2)

# convert gamma and epsilon to decimal
gamma_rate_dec = convert_to_dec(gamma_rate_string)
epsilon_rate_dec = convert_to_dec(epsilon_rate_string)

# calculate power consumption
power_consumption = gamma_rate_dec * epsilon_rate_dec
print(power_consumption)

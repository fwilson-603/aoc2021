# Advent of Code 2021; Dec 6, first puzzle

# SUCCESSFULLY SUBMITTED

# import needed material
import statistics
import collections
from collections import Counter

# read in the data
# load data
input = open("dec6-input.txt", "r")
data = input.read()

fish_list = data.split(",")
fish_list = [int(i) for i in fish_list]

# organize the list of fish as nested lists/dictionaries
# [(1, 234), (2, 33), ...] etc
counted_list = Counter(fish_list)
temp_list = Counter()

print(counted_list)

# loop through the list a set number of times, changing the numbers appropriately
for i in range(256):
    for x in range(9):
        if x == 0:
            temp_number = counted_list[x]
            temp_list[6] = temp_number
            temp_list[8] = temp_number
        elif x == 7:
            temp_number = counted_list[x]
            temp_list[6] += temp_number
        else:
            temp_number = counted_list[x]
            temp_list[x-1] = temp_number
    counted_list = temp_list.copy()

# at the end of the iteration, loop through to count the numbers
fish_count = 0

for y in counted_list:
    fish_count += counted_list[y]

print(fish_count)

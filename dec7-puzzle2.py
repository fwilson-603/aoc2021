# Advent of Code 2021; Dec 7, second puzzle

## SUCCESSFULLY SUBMITTED

# import needed material
import statistics

# load input file
input = open("dec7-input.txt", "r")
data = input.read()

# convert input to a list of integers
starting_positions = data.split(",")
starting_positions = [int(i) for i in starting_positions]

# find highest value in starting_positions
highest_value = max(starting_positions)

# evaluate all possible starting points 0 - (highest number)
target_results = []

for x in range(0, highest_value):
    fuel_use = 0
    for y in starting_positions:
        distance = abs(y - x)
        fuel_use += (distance*(distance + 1))/2
    target_results.append(fuel_use)

# find lowest value in target_results (i.e. lowest possible fuel use)
print(min(target_results))

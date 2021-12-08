# Advent of Code 2021; Dec 7, first puzzle

## SUCCESSFULLY SUBMITTED

# import needed material
import statistics

# load input file
input = open("dec7-input.txt", "r")
data = input.read()

# convert input to a list of integers
starting_positions = data.split(",")
starting_positions = [int(i) for i in starting_positions]
    
# find the geometric median (i.e. the target location)
target_location = round(statistics.median(starting_positions))

# starting fuel used is 0
fuel_use = 0

# loop through each crab position, absolute value of distance from
# median is fuel used to get to target location
for y in starting_positions:
    fuel_use += abs(y - target_location)

print(fuel_use)

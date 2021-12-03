# Advent of Code 2021; Dec 1, second puzzle

# load input file
input = open("dec1-input.txt", "r")

# store input file in an array
depths = []
for x in input:
    depths.append(int(x))

# generate sums, store in an array
sums = []

# loop go through every item in the array (except the last two)
# sum it with the two that follow, and add to the sums array
for y in range(0, len(depths)-2):
    current_sum = depths[y] + depths[y+1] + depths[y+2]
    sums.append(current_sum)

# check number of times sum of measurements has increased

# make a counter variable
increases = 0

# implement a loop to go through each number in the array;
# for each number in the array, if it is larger than the previous
# number, increase the counter variable
for i in range(1, len(sums)):
    if sums[i] > sums[i-1]:
        increases = increases + 1
        
# print the counter variable
print(increases)

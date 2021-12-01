# Advent of Code 2021; Dec 1, first puzzle

# Measuring depth increases

# load input file
input = open("dec1-input.txt", "r")

# store input file in an array
depths = []
for x in input:
    depths.append(int(x))
    
# make a counter variable
increases = 0

# implement a loop to go through each number in the array;
# for each number in the array, if it is larger than the previous
# number, increase the counter variable
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        increases = increases + 1
        
# print the counter variable
print(increases)

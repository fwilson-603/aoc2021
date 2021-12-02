# Advent of Code 2021; Dec 2, second puzzle

# load input file
input = open("dec2-input.txt", "r")

# set horizontal position, depth, and aim to '0'
horizontal = 0
depth = 0
aim = 0

# loop through each instruction, modifying position each time
for x in input:
    position_change = x.strip()
    direction = position_change[:-2]
    degree = int(position_change[-1:])
    if direction == "forward":
        horizontal += degree
        depth += aim * degree
    elif direction == "down":
        aim += degree
    elif direction == "up":
        aim -= degree

# multiply final horizontal position by final depth
final_position = horizontal * depth
print(final_position)

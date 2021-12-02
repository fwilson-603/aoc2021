# Advent of Code 2021; Dec 2, first puzzle

# load input file
input = open("dec2-input.txt", "r")

# set horizontal position and depth to '0'
horizontal = 0
depth = 0

# loop through each instruction, modifying position each time
for x in input:
    position_change = x.strip()
    direction = position_change[:-2]
    degree = int(position_change[-1:])
    if direction == "forward":
        horizontal += degree
    elif direction == "down":
        depth += degree
    elif direction == "up":
        depth -= degree

# multiply final horizontal position by final depth
final_position = horizontal * depth
print(final_position)

# Advent of Code 2021; Dec 6, first puzzle

## SUCCESSFULLY SUBMITTED

# read in the data
# load data
input = open("dec6-input.txt", "r")
data = input.read()

starting_fish_list = data.split(",")
starting_fish_list = [int(i) for i in starting_fish_list]

# setting fish_list to the starting point
# setting days to 0
fish_list = starting_fish_list.copy()
days = 0

# a function for fish breeding
def fish_breed():
    for x in range(len(fish_list)):
        if fish_list[x] > 0:
            fish_list[x] -= 1
        elif fish_list[x] == 0:
            fish_list[x] = 6
            fish_list.append(8)


# run the breeding cycle 80 times
for y in range(80):
    fish_breed()
    days += 1
    
## Warning, don't run more than 100 cycles or so, exponential growth
## is no joke

# length of the list is the output
print("After " + str(days) + " days, there are " + str(len(fish_list)) + " lanternfish")




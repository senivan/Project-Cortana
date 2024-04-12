# Problem: https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

# Prompt:
# Solve the following task in Python3:
# Build Tower

# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

# The result should be list, not a STRING


# Solution:
def tower_builder(n):
    space = ' '
    tower = []

    for i in range(1, n+1):
        tower.append((space*(n-i)+'*'+(2*i - 3)*'*'+space*(n-i)))

    return tower

# does not work as intended, need small fix in logic

# fixed solution:
def tower_builder(n):
    space = ' '
    tower = []

    for i in range(1, n+1):
        tower.append((space*(n-i)+'*'+(2*i - 2)*'*'+space*(n-i)))

    return tower

# passed all the test cases

#Comments:
# Ai was pretty close to the solution, probably small misunderstanding in the prompt.
# Logic is correct, just needed to adjust the number of '*' in each row.
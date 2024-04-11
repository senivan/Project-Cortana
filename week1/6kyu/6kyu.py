"""
Prompt: Build a pyramid-shaped tower, as an array/list of strings, 
given a positive integer number of floors. A tower block is represented with "*" character.
---
Copilot gave perfect solution for this problem from the first try.
Code:
"""
def tower_builder(floors):
    tower = []
    for floor in range(1, floors + 1):
        spaces = ' ' * (floors - floor)
        block = '*' * (2*floor - 1)
        tower.append(spaces + block + spaces)
    return tower
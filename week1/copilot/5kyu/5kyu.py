"""
Prompt: We want to write calculations using functions and get the results. 
Please write functions for numbers 0-9 and plus, minus, multiplicate and divide
Here are some examples:
seven(times(five())) # must return 35 
four(plus(nine())) # must return 13 
eight(minus(three())) # must return 5 
six(divided_by(two())) # must return 3
---
Copilot gave perfect solution for this problem from the first try.
Code:
"""

def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda x: x*y
def divided_by(y): return lambda x: x//y
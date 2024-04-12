# Problem : https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

# Prompt:
# Solve the following task in Python3:
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

# Solution:
def zero():
    return 0
def one():
    return 1
def two():
    return 2
def three():
    return 3
def four():
    return 4
def five():
    return 5
def six():
    return 6
def seven():
    return 7
def eight():
    return 8
def nine():
    return 9
def plus(num):
    return lambda num2: num+num2
def minus(num):
    return lambda num2: num-num2
def times(num):
    return lambda num2: num*num2
def divided_by(num):
    return lambda num2: num//num2

# Comments:
# AIs solution is not working. It is failing when unpaacking the last function call.
# Should be a pretty easy fix

# Fixed Solution:
def zero(func=None):
    if func is not None:
        return func(0)
    return 0
def one(func=None):
    if func is not None:
        return func(1)
    return 1
def two(func=None):
    if func is not None:
        return func(2)
    return 2
def three(func=None):
    if func is not None:
        return func(3)
    return 3
def four(func=None):
    if func is not None:
        return func(4)
    return 4
def five(func=None):
    if func is not None:
        return func(5)
    return 5
def six(func=None):
    if func is not None:
        return func(6)
    return 6
def seven(func=None):
    if func is not None:
        return func(7)
    return 7
def eight(func=None):
    if func is not None:
        return func(8)
    return 8
def nine(func=None):
    if func is not None:
        return func(9)
    return 9
def plus(num):
    return lambda num2: num2+num
def minus(num):
    return lambda num2: num2-num
def times(num):
    return lambda num2: num2*num
def divided_by(num):
    return lambda num2: num2//num
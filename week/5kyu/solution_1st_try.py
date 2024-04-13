def zero():
    """Returns the number zero"""
    return 0

def one():
    """Returns the number one"""
    return 1

def two():
    """Returns the number two"""
    return 2

def three():
    """Returns the number three"""
    return 3

def four():
    """Returns the number four"""
    return 4

def five():
    """Returns the number five"""
    return 5

def six():
    """Returns the number six"""
    return 6

def seven():
    """Returns the number seven"""
    return 7

def eight():
    """Returns the number eight"""
    return 8

def nine():
    """Returns the number nine"""
    return 9

def plus(a):
    """
    Defines addition operation. Takes a function (number) as argument 
    and returns a function that adds that number to another number.
    """
    def add(b):
        return a() + b()
    return add

def minus(a):
    """
    Defines subtraction operation. Takes a function (number) as argument 
    and returns a function that subtracts that number from another number.
    """
    def subtract(b):
        return a() - b()
    return subtract

def times(a):
    """
    Defines multiplication operation. Takes a function (number) as argument 
    and returns a function that multiplies that number by another number.
    """
    def multiply(b):
        return a() * b()
    return multiply

def divided_by(a):
    """
    Defines integer division operation. Takes a function (number) as argument 
    and returns a function that performs integer division on another number.
    """
    def divide(b):
        return a() // b()  # Use // for integer division
    return divide

# Example calculations (without parentheses after number functions)
print(seven(times(five())))  # Output: 35
print(four(plus(nine())))  # Output: 13
print(eight(minus(three())))  # Output: 5
print(six(divided_by(two())))  # Output: 3

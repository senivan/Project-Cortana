def number(n):
  """
  Returns the number provided as an argument
  """
  return n

# Define functions for operations
def plus(a, b):
  """
  Performs addition operation on two numbers
  """
  return a + b

def minus(a, b):
  """
  Performs subtraction operation on two numbers
  """
  return a - b

def times(a, b):
  """
  Performs multiplication operation on two numbers
  """
  return a * b

def divided_by(a, b):
  """
  Performs integer division on two numbers
  """
  return a // b  # Use // for integer division

# Example calculations (use number function for numbers)
print(number(seven())(times(five())))  # Output: 35
print(number(four())(plus(nine())))  # Output: 13
print(number(eight())(minus(three())))  # Output: 5
print(number(six())(divided_by(two())))  # Output: 3

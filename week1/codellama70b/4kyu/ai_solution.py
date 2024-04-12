# Problem : https://www.codewars.com/kata/59016379ee5456d8cc00000f/train/python

# Prompt:
# Solve task in Python3
# Task

# Since the weather was good, some students decided to go for a walk in the park after the first lectures of the new academic year. There they saw a squirrel, which climbed a tree in a spiral at a constant angle to the ground. They calculated that in one loop the squirrel climbes h meters (vertical height), the height of the tree is equal to H (v in Ruby), and the length of its circumference equals S.

# These calculations were exhausting, so now the students need your help to figure out how many meters the path length of squirrel climbed when it reached the tree top. The result should be rounded to 4 decimal places.

# Code Limit

# Less than 52 characters

# Example

# For h = 4, H = 16, S = 3, the output should be 20.

# For h = 8, H = 9, S = 37, the output should be 42.5869.

# Check your formula. You can not import any libraries

# Solution one:

def answer(h,H,S):
    # your code here
    x=1;
    while (x<=H-h):
        x+=((S*h)/2)**0.5
    
    return round(x,4);

# Comments:
# The formula is not correct. The formula should be (h**2+S**2)**0.5*H/h
# I tried many prompts, but the AI will not use the correct formula, unless explicitly told to do so.

# Prompt with correct formula:
# Solve task in Python3
# Task

# Since the weather was good, some students decided to go for a walk in the park after the first lectures of the new academic year. There they saw a squirrel, which climbed a tree in a spiral at a constant angle to the ground. They calculated that in one loop the squirrel climbes h meters (vertical height), the height of the tree is equal to H (v in Ruby), and the length of its circumference equals S.

# These calculations were exhausting, so now the students need your help to figure out how many meters the path length of squirrel climbed when it reached the tree top. The result should be rounded to 4 decimal places.

# Code Limit

# Less than 52 characters

# Example

# For h = 4, H = 16, S = 3, the output should be 20.

# For h = 8, H = 9, S = 37, the output should be 42.5869.

# Here is formula you should use: (h**2+S**2)**0.5*H/h. You can not import any libraries

# Solution two:
def answer(h, H, S):
    # your code here
    x = (((h ** 2 + S ** 2) ** 0.5) * H / h);
    
    return round(x,4);

# Comments:
# The AI is now using the correct formula. The solution is now correct, though it needs to be smaller than 52 characters which ai fails to do.
# after asking it to make it smaller, it will remove the spaces and make the code smaller than 52 characters.

# Final Solution:
squirrel=lambda h,H,S:round((h**2+S**2)**0.5*H/h,4)

"""
Old code:
"""
x = int(input())

print('*')
if x>1:
    print('*'*2)

if x>3:
    print('*','*')

for i in range(4,x):
    print('*',' '*(i-4),'*')

if x>2:
    print('*'*x)
"""
New code:
Prompt: rewrite this code from scratch so the output is:
*
**
* *
*  *
*   *
******
Comments:
Copilot needed a few tries to get the code right and a bit of help with the last line, but the final version is correct.
"""
x = int(input())

for i in range(1, x+1):
    if i == x:
        print('*' * x)
    else:
        print('*' + ' ' * (i-2) + '*' if i > 1 else '*')

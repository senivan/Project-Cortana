# початковий код
# x = int(input())
# print('*')
# if x>1:
#     print('*'*2)
# if x>3:
#     print('*','*')
# for i in range(4,x):
#     print('*',' '*(i-4),'*')
# if x>2:
#     print('*'*x)

# код аі до якого вдалось дійти
x = int(input())
for i in range(1, x + 1):
    # Print leading spaces for proper indentation
    print(" " * (x - i), end="")
    # Print stars for each row
    print("*" * (2 * i - 1))


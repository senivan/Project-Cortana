# не оптимізований власний код
def calculate_expression(expression:str) -> int:
    """
    (str) -> int
    Write a calculate_expression function that will take a single argument - 
    a string with a simple mathematical expression and return 
    an integer - the result of this expression.
    >>> calculate_expression('Скільки буде 8 відняти 3?')
    5
    >>> calculate_expression('Скільки буде 8 мінус 3?')
    5
    >>> calculate_expression('Скільки буде 3 помножити на 2 додати 7?')
    13
    >>> calculate_expression('Скільки буде 10 поділити на -2 додати 11 мінус -4?')
    10
    >>> calculate_expression('Скільки буде 10 розділити на 2?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 10 поділити на 2?')
    5.0
    >>> calculate_expression('Скільки коштує цибуля?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 5 помножити на 4 помножити на 3 помножити на 2 помножити на 1 відняти 120 мінус 5?')
    -5
    >>> calculate_expression('Скільки буде 3 помножити на 0 поділити на 3?')
    0.0
    >>> calculate_expression('Скільки буде 10 поділити на 0?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 10 9 додати?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 10 додати додати 9?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 9 9?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 2?')
    2
    >>> calculate_expression('3 плюс 2?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 10 поділити на 2')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде -10 поділити на 2 помножити на 3?')
    -15
    >>> calculate_expression('Скільки буде -10 поділити на помножити на 3?')
    'Неправильний вираз!'
    """
    if isinstance(expression,str):
        znak_lst = ['+','-','*','/']
        ex = expression
        result = 0
        expression_r = expression.replace('Скільки буде ','')
        expression_r = expression_r.replace('?','')
        expression_r = expression_r.replace('відняти','-')
        expression_r = expression_r.replace('мінус','-')
        expression_r = expression_r.replace('додати','+')
        expression_r = expression_r.replace('плюс','+')
        expression_r = expression_r.replace('помножити на','*')
        expression_r = expression_r.replace('поділити на','/')
        exp_lst = expression_r.split(' ')
        if len(exp_lst) == 1:
            return int(exp_lst[0])
        if (ex.count('відняти') == 0 and ex.count('мінус') == 0 and ex.count('додати') == 0
        and ex.count('плюс')==0 and ex.count('помножити на')==0 and ex.count('поділити на')==0):
            return 'Неправильний вираз!'
        if ex.count('?') != 1 or ex.count('Скільки буде ') != 1:
            return 'Неправильний вираз!'
        while len(exp_lst) > 1:
            if (exp_lst[1] == '+' and exp_lst[0] not in znak_lst and exp_lst[2] not in znak_lst):
                result = int(exp_lst[0]) + int(exp_lst[2])
                exp_lst = exp_lst[3::]
                exp_lst.insert(0,result)
                continue
            if (exp_lst[1] == '-' and exp_lst[0] not in znak_lst and exp_lst[2] not in znak_lst):
                result = int(exp_lst[0]) - int(exp_lst[2])
                exp_lst = exp_lst[3::]
                exp_lst.insert(0,result)
                continue
            if (exp_lst[1] == '*' and exp_lst[0] not in znak_lst and exp_lst[2] not in znak_lst):
                result = int(exp_lst[0]) * int(exp_lst[2])
                exp_lst = exp_lst[3::]
                exp_lst.insert(0,result)
                continue
            if (exp_lst[1] == '/' and exp_lst[0] not in znak_lst and exp_lst[2] not in znak_lst):
                if exp_lst[2] == '0':
                    return 'Неправильний вираз!'
                result = int(exp_lst[0]) / int(exp_lst[2])
                exp_lst = exp_lst[3::]
                exp_lst.insert(0,result)
                continue
            return 'Неправильний вираз!'
    return result

#код що видає аі
#на перших запитах ші рекомендує використання бібліотеки re проте код не
# робочий взагалі, навіть після 15 запитів з прикладами того як має працювати функція

# import re
# def calculate_expression(expression: str) -> int or float:
#   if not isinstance(expression, str):
#       return "Неправильний вираз!"
#   expression = expression.lower().replace("скільки буде ", "").replace("?", "")
#   expression = expression.replace("відняти", "-").replace("мінус", "-")
#   expression = expression.replace("додати", "+").replace("плюс", "+")
#   expression = expression.replace("помножити на", "*").replace("поділити на", "/")
#   if not re.match(r"^\d+(?:[\+\-\*/]\d+)*$", expression):
#       return "Неправильний вираз!"
    # if re.match(r"^\d+$", expression):
#       return int(expression)
#   def evaluate(expr):
#       if not expr:
#           return None
#       tokens = expr.split()
#       operand1 = int(tokens[0])
#       operator = tokens[1]
#       operand2 = int(tokens[2])
#       if operator == "+":
#           return evaluate(expr[4:]) + operand1
#       elif operator == "-":
#           return evaluate(expr[4:]) - operand1
#       elif operator == "*":
#           return operand1 * evaluate(expr[4:])
#       elif operator == "/":
#           if operand2 == 0:
#               return "Неправильний вираз! Ділення на нуль."  # Division by zero error message in Ukrainian
#           return operand1 / evaluate(expr[4:])
#       else:
#           return "Неправильний вираз!"
#   result = evaluate(expression)
#   if isinstance(result, float) and result == 0.0:
#       return 0
#   else:
#       return result

# на запит спробувати піти іншим шляхом розв'язання так як з модулем дійти до правильного висновку не вийшло
# def calculate_expression(expr: str) -> int or str:
#     """
#     >>> calculate_expression('Скільки буде 8 відняти 3?')
#     5
#     >>> calculate_expression('Скільки буде 8 мінус 3?')
#     5
#     >>> calculate_expression('Скільки буде 3 помножити на 2 додати 7?')
#     13
#     >>> calculate_expression('Скільки буде 10 поділити на -2 додати 11 мінус -4?')
#     10
#     >>> calculate_expression('Скільки буде 10 розділити на 2?')
#     'Неправильний вираз!'
#     >>> calculate_expression('Скільки буде 10 поділити на 2?')
#     5.0
#     >>> calculate_expression('Скільки коштує цибуля?')
#     'Неправильний вираз!'
#     >>> calculate_expression('Скільки буде 5 помножити на 4 помножити на 3 помножити на 2 помножити на 1 відняти 120 мінус 5?')
#     -5
#     >>> calculate_expression('Скільки буде 3 помножити на 0 поділити на 3?')
#     0.0
#     >>> calculate_expression('Скільки буде 10 поділити на 0?')
#     'Неправильний вираз!'
#     >>> calculate_expression('Скільки буде 10 9 додати?')
#     'Неправильний вираз!'
#     >>> calculate_expression('Скільки буде 10 додати додати 9?')
#     'Неправильний вираз!'
#     >>> calculate_expression('Скільки буде 9 9?')
#     'Неправильний вираз!'
#     >>> calculate_expression('Скільки буде 2?')
#     2
#     >>> calculate_expression('3 плюс 2?')
#     'Неправильний вираз!'
#     >>> calculate_expression('Скільки буде 10 поділити на 2')
#     'Неправильний вираз!'
#     >>> calculate_expression('Скільки буде -10 поділити на 2 помножити на 3?')
#     -15
#     >>> calculate_expression('Скільки буде -10 поділити на помножити на 3?')
#     'Неправильний вираз!'
#     """
#     if not expr:
#         return None
#     stack = []
#     for token in expr.split():
#         if token.isdigit():
#             stack.append(int(token))
#         elif token in ["+", "-", "*", "/"]:
#             operand2 = stack.pop()
#             operand1 = stack.pop()  # Stack-based approach for order of operations
#             if token == "+":
#                 stack.append(operand1 + operand2)
#             elif token == "-":
#                 stack.append(operand1 - operand2)
#             elif token == "*":
#                 stack.append(operand1 * operand2)
#             elif token == "/":
#                 if operand2 == 0:
#                     return "Неправильний вираз! Ділення на нуль."
#                 stack.append(operand1 / operand2)
#             else:
#                 return "Неправильний вираз!"
#     if len(stack) != 1:
#         return "Неправильний вираз!"
#     return stack[0]

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

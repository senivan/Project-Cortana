"""Lab №5_4"""

# Copilot was losing important cases while trying to optimize this code.
# It took him a lot of promts to add checks and make the code work
# and pass all the tests. He used eval, thus shortening the code.
# He also found it difficult to work with code containing Ukrainian expressions.
# In the end, the code runs correctly, but not much faster than the original version.

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
    # Dictionary to translate Ukrainian words to English
    translate_dict = {
        'Скільки буде': '',
        'відняти': '-',
        'мінус': '-',
        'помножити на': '*',
        'додати': '+',
        'плюс': '+',
        'поділити на': '/',
        '?': ''
    }

    if 'Скільки буде' not in expression or '?' not in expression:
        return 'Неправильний вираз!'

    operation_words = ['відняти', 'мінус', 'помножити на', 'додати', 'поділити на']
    for word in operation_words:
        if word + ' ' + word in expression:
            return 'Неправильний вираз!'

    last_operation_is_division = 'поділити' in expression.split()[-3]

    for ukr, eng in translate_dict.items():
        expression = expression.replace(ukr, eng)

    try:
        result = eval(expression.strip())
        if not last_operation_is_division:
            return int(result)
        return result
    except (SyntaxError, ZeroDivisionError):
        return 'Неправильний вираз!'

if __name__ == "__main__":
    import doctest
    print(doctest.testmod(verbose=False))

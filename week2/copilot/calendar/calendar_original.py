'''
Module to generate calendar for one month
https://github.com/DoktorTomato/Shevchuk-Ivan-lab8-task1
'''
from benchmark_funcs import time_to_run, memory_used
import datetime
import calendar as cal

def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]
        
    >>> weekday_name(3)
    'thu'
    """
    days_of_the_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    return days_of_the_week[number]

def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError 
    with corresponding message
                                                
    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    >>> weekday('22.10.2017')
    6
    >>> weekday('07.03.2003')
    4
    >>> weekday('04.11.2023')
    5
    """
    date_lst = date.split('.')
    day = int(date_lst[0])
    month_ = int(date_lst[1])
    year_ =  int(date_lst[2])
    return datetime.date(year_, month_, day).weekday()
@memory_used
def calendar(this_month: int, this_year: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    
     Time taken: calendar 2.7293209026538534e-05
     Memory: calendar (1072, 6316)
     
    """
    cal_str = cal.month(this_year, this_month, 3).rstrip()
    cal_str = cal_str.lower()
    cal_lst = cal_str.split('\n')
    cal_lst.pop(0)
    res = ''
    for line in cal_lst:
        res += f'{line}\n'
    res = res.rstrip()
    return res
@memory_used
def transform_calendar(calendar_: str) -> str:
    """Return a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print(transform_calendar(calendar(5, 2002)))
    mon   6 13 20 27
    tue   7 14 21 28
    wed 1 8 15 22 29
    thu 2 9 16 23 30
    fri 3 10 17 24 31
    sat 4 11 18 25
    sun 5 12 19 26
    >>> print(transform_calendar(calendar(8 , 2015)))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30

    Time taken: transform_calendar 6.6185030227643435e-06
    Memory: transform_calendar (160, 3272)
    """
    tmp_lst = calendar_.split('\n')
    cal_lst = []
    res_lst = []
    res = ''
    for line in tmp_lst:
        line = line.replace('    ', '_ ')
        line = line.split()
        cal_lst.append(line)
    for i in range(7):
        vert_line = []
        for line_ in cal_lst:
            try:
                if line_[i] == '_':
                    vert_line.append(' ')
                else:
                    vert_line.append(line_[i])
            except IndexError:
                continue
        res_lst.append(vert_line)
    for vert in res_lst:
        for ind, el in enumerate(vert):
            if ind == len(vert) - 1:
                res += f'{el}'
            else:
                res += f'{el} '
        res += '\n'
    res = res.rstrip()
    return res

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print (transform_calendar(calendar(month, year)))
    except ValueError as err:
        print(err)

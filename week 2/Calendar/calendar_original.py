'''
Module to generate calendar for one month
https://github.com/DoktorTomato/Shevchuk-Ivan-lab8-task1
'''
import datetime

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
    month = int(date_lst[1])
    year =  int(date_lst[2])
    return datetime.date(year, month, day).weekday()

def calendar(month: int, year: int) -> str:
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
    """
    cal_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    cal_lst = []
    line = 0
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            number_of_days = 31
        case 2:
            if year % 4 == 0:
                number_of_days = 29
            else:
                number_of_days = 28
        case _:
            number_of_days = 30
    for date in range(1, number_of_days+1):
        cal_dict[weekday(f'{date}.{month}.{year}')].append(date)
    day = 1
    while day != number_of_days+1:
        weekd = weekday(f'{day}.{month}.{year}')
        if weekd == 0 and day==number_of_days:
            line += 1
        if weekd == 6:
            line += 1
        day += 1
    for _ in range(line):
        cal_lst.append([[]]*7)
    return cal_lst


def transform_calendar(calendar: str) -> str:
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
    """
    pass


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    # try:
    #     print("Type month")
    #     month = input()
    #     month = int(month)
    #     print("Type year")
    #     year = input()
    #     year = int(year)
    #     print("\n\nThe calendar is: ")
    #     print (calendar(month, year))
    # except ValueError as err:
    #     print(err)

"""
Module to generate calendar for one month

Adapted from: https://github.com/DoktorTomato/Shevchuk-Ivan-lab8-task1
"""

import datetime
import calendar as cal
from benchmark_funcs import time_to_run, memory_used

@time_to_run
def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun").

    Args:
        number: An integer in range [0, 6].

    Returns:
        The weekday name as a string.

    >>> weekday_name(3)
    'thu'

    Time taken: weekday_name 3.603007644414902e-07
    Memory: weekday_name (0, 64)
    """

    days_of_the_week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    return days_of_the_week[number]

@time_to_run
def weekday(date: str) -> int:
    """
    Return an integer representing a weekday (0 represents Monday and so on).

    Uses Zeller's Congruence algorithm.

    Args:
        date: A string of the form "day.month.year".

    Raises:
        AssertionError: If the date is invalid.

    Returns:
        The weekday as an integer (0-6).

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

    Time taken: weekday 1.3692998327314854e-06
    Memory: weekday (48, 359)
    """

    try:
        date_list = date.split(".")
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
        return datetime.date(year, month, day).weekday()
    except ValueError:
        raise ValueError("Invalid date format. Please use DD.MM.YYYY")

@time_to_run
def calendar(month: int, year: int) -> str:
    """
    Return a string representing a horizontal calendar for the given month and year.

    Args:
        month: An integer in range [1, 12].
        year: An integer (strictly speaking the algorithm in weekday works correctly
              only for Gregorian calendar, so year must be greater than 1583).

    Raises:
        AssertionError: If arguments are invalid.

    Returns:
        The calendar as a string.

    >>> print(calendar(8, 2015))
    mon tue wed thu fri sat sun
           1   2
     3   4   5   6   7   8   9
    10  11  12  13  14  15  16
    17  18  19  20  21  22  23
    24  25  26  27  28  29  30
    31

    Time taken: calendar 0.00010685570084024221
    Memory: calendar (1512, 2906)
    """

    if not (1 <= month <= 12):
        raise AssertionError("Month must be between 1 and 12")
    if year < 1583:
        raise AssertionError("Year must be greater than 1583")

    cal_str = cal.month(year, month, 3).rstrip().lower()
    cal_list = cal_str.splitlines()
    cal_list.pop(0)
    return "\n".join(cal_list)

@time_to_run
def transform_calendar(calendar_str: str) -> str:
    """
    Return a modified horizontal -> vertical calendar, ensuring correct first day placement, 
    single Monday per week, proper day alignment, and handling of extra empty lines.

    Args:
        calendar_str: A string of a calendar, returned by the calendar() function.

    Returns:
        The transformed calendar as a string (vertical format).

    Time taken: transform_calendar 3.07081004139036e-05
    Memory: transform_calendar (224, 2547)
    """

    calendar_list = calendar_str.splitlines()
    weekday_list = calendar_list.pop(0).split()  # Extract weekdays from first line
    result = [[] for _ in range(7)]  # Initialize 7 empty lists for weekdays

    # Check if first day is Sunday and adjust weekday list and result
    if calendar_list[0].split()[0] != weekday_list[0]:
        weekday_list.append(weekday_list.pop(0))  # Rotate weekdays if Sunday starts
        result.append([])  # Add empty list for Sunday

    # Process first line to handle Sunday start and populate result with actual days
    first_line_days = [int(day) for day in calendar_list[0].split()[1:]]  # Convert days to integers
    for i, day in enumerate(first_line_days):
        try:
            result[(i + 1) % 7].append(day)  # Append with offset for Sunday start
        except IndexError:
            pass

    # Process remaining lines, skipping the first
    for line in calendar_list[1:]:
        monday_found = False
        for i, day in enumerate(line.split()[1:]):
            if not monday_found and day != 0:  # Check for Monday and avoid empty days
                monday_found = True
                result[i].append(int(day))  # Append day as integer
            elif day != 0:  # Append non-empty days after first Monday
                result[(i + 1) % 7].append(int(day))  # Append day as integer

    # Format and return the final calendar string with proper day alignment, handling extra empty lines
    final_calendar = ""
    max_len = max(len(line) for line in result if line)  # Find the maximum length of non-empty weeks

    for i, line in enumerate(result):
        if not line:  # Skip empty lines (including the potentially added Sunday line)
            continue
        weekday = weekday_list[i % len(weekday_list)]  # Get weekday name
        padding = " " * (max_len - len(line))  # Calculate padding based on maximum week length

        # Add a non-breaking space (`\u00A0`) before the first day for proper alignment
        final_calendar += f"{weekday}\u00A0{' '.join(str(day) for day in line)}{padding}\n"

    return final_calendar.rstrip()

if __name__ == '__main__':
    weekday_name(3)
    weekday("12.08.2015")
    calendar(5, 2002)
    print(transform_calendar('mon tue wed thu fri sat sun\n           1   2\n     3   4   5   6   7   8   9\n    10  11  12  13  14  15  16\n    17  18  19  20  21  22  23\n    24  25  26  27  28  29  30\n    31'))

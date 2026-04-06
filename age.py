# short program that calculates the age between the current date and given date
# when given a date
# e.g. 01-01-1990 returns 31, 04-12-1972 returns 48
# needs to be useable from iTerm so needs to be able to add input from terminal?

from datetime import datetime as dt


def get_years_passed() -> int:
    input_date = input("Input a date in the format day-month-year: ")
    input_date = dt.strptime(input_date, "%d-%m-%Y")
    today = dt.today()
    difference = (today - input_date).days
    # return the number of years
    return int(difference // 365.25)


# testing
print(get_years_passed())

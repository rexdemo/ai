import calendar


def display_calendar(year, month):
    print(calendar.month(year, month))


year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

display_calendar(year, month)

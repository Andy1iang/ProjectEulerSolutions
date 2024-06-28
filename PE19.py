# https://projecteuler.net/problem=19

from TimeCode import timeCode


def PE19():

    month = 1
    year = 1901
    day = 2
    count = 0

    # while we are not at target year yet
    while year <= 2000:

        # months with 31 days
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            day += 31

        # months with 30 days
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day += 30

        # taking into account for wacky Feb
        elif month == 2:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        day += 29
                    else:
                        day += 28
                else:
                    day += 29
            else:
                day += 28

        # iterating through each months and updating the days
        month += 1
        if month > 12:
            month = 1
            year += 1

        day = day % 7

        if day == 0:
            count += 1

    print(count)


timeCode(PE19)

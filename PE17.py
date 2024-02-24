# https://projecteuler.net/problem=17

from TimeCode import timeCode

# the length of the numbers if written out in owrds
singles = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
           10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
doubles = {20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}


def projectEuler17():

    letterCount = 0
    for i in range(1, 1000):

        temp = i

        if i < 20:
            letterCount += singles[temp]

        elif i < 100:
            letterCount += singles[temp % 10]
            temp = temp // 10
            letterCount += doubles[temp*10]

        else:
            letterCount += 10
            letterCount += singles[i//100]
            temp = temp % 100
            if temp < 20:
                letterCount += singles[temp]

            elif temp < 100:
                letterCount += singles[temp % 10]
                letterCount += doubles[(temp//10)*10]

    letterCount += 11  # accounting for one thousand
    letterCount -= 3*9  # account for the extra 'and' for the hundreds

    print(letterCount)


timeCode(projectEuler17)

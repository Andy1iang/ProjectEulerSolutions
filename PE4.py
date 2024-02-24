# https://projecteuler.net/problem=4

from TimeCode import timeCode


def projectEuler4():

    largest = 0

    for i in range(999, 99, -1):  # checking all triple digit numbers
        for j in range(999, 99, -1):
            if str(i*j) == str(i*j)[::-1]:
                # checking if it's the largest palindrome
                largest = max(largest, i*j)
                
    print(largest)


timeCode(projectEuler4)

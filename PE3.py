# https://projecteuler.net/problem=3

from TimeCode import timeCode


def projectEuler3():

    # prime factorization
    def primeFac(num, divisor): 

        # looping from lowest possible divisor to sqrt of numerator
        for i in range(divisor, int(num**0.5)+1):
            if num % i == 0:
                # recursive call when we find a prime factor
                return (primeFac(num/i, i))

        return int(num)

    print(primeFac(600851475143, 2))


timeCode(projectEuler3)

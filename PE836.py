# https://projecteuler.net/problem=836
# aprilsfoolsjoke

from TimeCode import timeCode

words = ['affine', 'plane', 'radically', 'integral', 'local', 'field', 'open',
         'oriented', 'line', 'section', 'jacobian', 'orthogonal', 'kernel', 'embedding']


def projectEuler836():

    print(getLetter(words))


def getLetter(words):

    if len(words) == 0:
        return ''

    else:
        return words[0][0] + getLetter(words[1:])


timeCode(projectEuler836)

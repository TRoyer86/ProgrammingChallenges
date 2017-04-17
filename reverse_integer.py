'''
author - Tatyana Royer
-------------
Take an integer and reverse it. Return 0 if it exceeds representation
by a 32 bit signed number.
'''

def reverse(self, x):
    result = 0
    if x > 0:
        while x != 0:
            result = (10*result) + (x % 10)
            x = x // 10
        if result < ((2**31)-1):
            return result
        else:
            return 0
    if x == 0:
        return 0
    if x < 0:
        x = (-1 * x)
        while x != 0:
            result = (10*result) + (x % 10)
            x = x // 10
        if result < ((2**31)-1):
            return (-1) * result
        else:
            return 0

if __name__ == '__main__':

    print(reverse(123))
    print(reverse(98976769876789))
    print(reverse(-123))


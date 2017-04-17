def isPalindrome(self, x):
    result = 0
    temp = x
    if x > 0:
        while x != 0:
            result = (10*result) + (x % 10)
            x = x // 10
        return temp == result
    elif x == 0:
        return True
    else:
        return False
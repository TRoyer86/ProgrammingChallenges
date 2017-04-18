def myPow(x, n):

    if n == 0:
        return 1
    else:
        return x * myPow(x, n-1)

if __name__ == '__main__':

    print(myPow(2, 4))

import random


def check(a, s, d, n):
    x = pow(a,d,n)
    print("%3d --> %3d" % (a, x))
    if x == 1:
        return True
    for i in range(s-1):
        if x == n-1:
            return True
        x = pow(x,2,n)
    return x == n-1


def miller_rabin(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = n-1
    s = 0
    while not 1 & d:
        d >>= 1
        s += 1
    for i in range(k):
        a = random.randrange(2, n-1)
        if not check(a, s, d, n):
            return False
    return True


n = int(input("Enter N: "))
k = int(input("Enter a suitable number of iterations: "))
print(miller_rabin(n, k))

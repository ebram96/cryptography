def large_mod(a, b, n):
    c = 0
    f = 1
    two_pow = 1
    while two_pow <= b:
        two_pow <<= 1
    two_pow >>= 1
    while two_pow:
        c *= 2
        f = (f * f) % n
        if two_pow & b:
            c = c+1
            f = (f * a) % n
        two_pow >>= 1
    return f


print("Enter base: ")
a = int(input())
print("Enter power: ")
b = int(input())
print("Enter N: ")
n = int(input())

print(large_mod(a, b, n))

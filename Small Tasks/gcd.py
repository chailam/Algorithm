"""
Name : Loi Chai Lam
Date : 5/3/2018
Write a program to compute the greatest common divisor (GCD) of
two positive numbers.

Explore more efficient ways to compute GCD of two positive numbers.

"""

def gcd1(a,b):
    # O(log(n))
    while b > 0:
        a,b = b,a%b
    return a

def gcd2(a,b):
    # O(log(n))
    if (a == 0 and b != 0):
        return b
    elif(a != 0 and b == 0):
        return a
    else:
        return gcd(b,a%b)


def gcd_good(a,b):
    break


print(gcd1(10,20))

    

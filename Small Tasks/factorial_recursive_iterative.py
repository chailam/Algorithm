"""
Name : Loi Chai Lam
Date : 5/3/2018
Write a program to compute the factorial of a number recursively.
Write an iterative version of the same.

Both also O(n), but recursive memory space is o(N), iterative memory space is O(1)

"""

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * fac_rec(n-1)


def factorial_iterative(n):
    total = 1
    while (n > 0):
        total = total * n
        n = n - 1
    return total



print(factorial_recursive(5))
print(factorial_iterative(5))




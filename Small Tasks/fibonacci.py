"""
Name : Loi Chai Lam
Date : 5/3/2018
Given some N ≥ 0 as a command line parameter, write a program to
compute the Nth number in the sequence of a Fibonacci

Explore more efficient ways to compute Nth number in the Fibonacci
sequence.


"""


def fibonacci_recursive(n):
    #O(2^n)
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def fibonacci(n):
    #O(n)
    return fibonacci_aux(n,0,1)

def fibonacci_aux(n,beforelast,last):
    if n == 0:
        return beforelast
    else:
        return fib_aux(n-1,last,beforelast+last)

    
def fibonacci_iterative(n):
    a = 0
    b = 1
    for i in range(0,n,1):
        a = a + b
        b = a - b
        return a

def fibonacci_good(n):
    """
    magic matrix!
    O(log(n))
    [[1,1],[1,0]] continuous multiply [F2,F1].
    N^8 = N*N*N*N...*N   <<multiply 8 times
        = ((N^2)^2)^2   <<multiply 3 times
    
    """

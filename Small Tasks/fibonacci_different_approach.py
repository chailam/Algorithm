"""
Name : Loi Chai Lam
Date : 5/3/2018
Given some N ≥ 0 as a command line parameter, write a program to
compute the Nth number in the sequence of a Fibonacci

Explore more efficient ways to compute Nth number in the Fibonacci
sequence.
1. Fibonacci Recursive Version 1
2. Fibonacci Recursive Version 2
3. Fibonacci Iterative
4. Fibonacci Dynamic Programming Top Down
5. Fibonacci Dynamic Programming Bottom Up 

"""

# ================Fibonacci Recursive Version 1=======================#


def fibonacci_recursive(n):
    """
    O(2^n)
    """
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)

# ================Fibonacci Recursive Version 2=======================#


def fibonacci(n):
    """
    O(n)
    """
    return fibonacci_aux(n, 0, 1)


def fibonacci_aux(n, beforelast, last):
    if n == 0:
        return beforelast
    else:
        return fibonacci_aux(n-1, last, beforelast+last)


# ================Fibonacci Iterative=======================#

def fibonacci_iterative(n):
    """
    O(n)
    """
    a = 0
    b = 1
    for i in range(0, n, 1):
        a = a + b
        b = a - b
    return a


# ================Fibonacci using Dynamic Programming Top Down=======================#
# the n-th fibonacci number to be found
n1 = 4

# initialize the tmp array with -1, including index 0
tmp_array1 = [-1] * (n1 + 1)

tmp_array1[0] = 0  # 0th finobacci value
tmp_array1[1] = 1  # 1st finobacci value


def fibonacci_dynamic_programming_top_down(n):
    """
    O(n)
    """
    if tmp_array1[n] != -1:
        return tmp_array1[n]
    else:
        tmp_array1[n] = fibonacci_dynamic_programming_top_down(n - 1) + fibonacci_dynamic_programming_top_down(n - 2)
        return tmp_array1[n]


# ================Fibonacci using Dynamic Programming Bottom Up=======================#


# the n-th fibonacci number to be found
n2 = 4

# initialize the tmp array with -1, including index 0
tmp_array2 = [-1] * (n2 + 1)

tmp_array2[0] = 0  # 0th finobacci value
tmp_array2[1] = 1  # 1st finobacci value


def fibonacci_dynamic_programming_bottom_up(n):
    """
    O(n)
    """
    for i in range(2, n + 1):
        tmp_array2[i] = tmp_array2[i - 1] + tmp_array2[i - 2]
    return tmp_array2[n]


# ================End=======================#
print(fibonacci_dynamic_programming_bottom_up(4))

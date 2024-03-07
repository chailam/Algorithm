"""
Author: Loi Chai Lam
Date: 6 Mar 2024
The Fibonacci Algorithm written in Dynamic Programming 
using Top Down and Bottom Up approach
"""

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


# the n-th  fibonacci number to be found
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

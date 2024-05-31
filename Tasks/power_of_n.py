"""
Name : Loi Chai Lam
Date : 14 Jun 2017

This program is to compute the power of n using for loop and recursive


"""


import random
import timeit


def powerOfN(x, n):
    """computes x to the power of n"""
    # This function is the code presented by David Albrecht in
    # Divide And Conquer: Lecture 13, FIT1045 Introduction to Algorithms and Programming,
    # Clayton Campus, Monash University, 10 May,2016.

    value = 1
    for k in range(n):
        value *= x
    return value


def powerOfNRecursive(x, n):
    """computes x to the power of n using recursive"""
    # This function is the code presented by David Albrecht in
    # Recursion: Lecture 14, FIT1045 Introduction to Algorithms and Programming,
    # Clayton Campus, Monash University, 10 May,2016.

    value = 1
    if n > 0:
        value = powerOfNRecursive(x, n // 2)
    if n % 2 == 0:
        value = value * value
    else:
        value = value * value * x
    return value

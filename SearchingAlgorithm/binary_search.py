"""
Author: Loi Chai Lam
Date: 25 May 2017

Binary Search

A searching algorithm for finding an element's position in a sorted array. 
In this approach, the element is always searched in the middle of a portion 
of an array. Binary search can be implemented only on a sorted list of items. 
If the elements are not sorted already, we need to sort them first.
"""


def binarySearch1(aList, target):
    low = 0
    high = len(aList) - 1
    while low <= high:
        middle = (low + high) // 2
        if aList[middle] == target:
            return middle
        elif aList[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return -1

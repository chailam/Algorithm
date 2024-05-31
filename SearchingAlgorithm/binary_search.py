"""
Author: Loi Chai Lam
Date: 25 May 2017

Binary Search

A searching algorithm for finding an element's position in a sorted array.
In this approach, the element is always searched in the middle of a portion
of an array. Binary search can be implemented only on a sorted list of items.
If the elements are not sorted already, we need to sort them first.
"""

# binary search using While


def binarySearch(aList, target):
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


# Binary Search using recursive

def binarySearchRecursive(aList, target, start, end):
    low = start
    high = end
    if low > high:
        return -1
    else:
        middle = (low + high) // 2
        if aList[middle] == target:
            return middle
        elif aList[middle] > target:
            return (binarySearchRecursive(aList, target, start, middle - 1))
        else:
            return (binarySearchRecursive(aList, target, middle + 1, end))

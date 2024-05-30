"""
Author: Loi Chai Lam
Date: 30 May 2024

Bubble Sort
Referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the input list element by element, 
comparing the current element with the one after it, swapping their values if needed

Complexity:
U –total numbers of item to be sorted, C - maximum number of characters in any item, 
K - maximum number of subitems in the item
Time complexity :worst : O(U)orU(K),for number ; O(UK),for characters
Space complexity : worst : O(UK),for number ; O(UCK),for characters
"""


def bubbleSort(the_list):
    n = len(the_list)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if the_list[j] > the_list[j + 1]:
                swap(the_list, j, j + 1)
                swapped = True
        if not swapped:
            break


def swap(the_list, j, i):
    tmp = the_list[j]
    the_list[j] = the_list[i]
    the_list[i] = tmp


the_list = [5, 8, 2, 0, 17, -1]
bubbleSort(the_list)
print(the_list)

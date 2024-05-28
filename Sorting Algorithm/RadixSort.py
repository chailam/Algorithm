"""
Author: Loi Chai Lam
Date: 28 May 2024

Radix Sort
A linear sorting algorithm that sorts elements by processing them digit by digit. 
It is an efficient sorting algorithm for integers or strings with fixed-size keys. 

It is utilizing the Counting Sort.


Complexity:
U –total numbers of item to be sorted, C - maximum number of characters in any item, 
K - maximum number of subitems in the item
Time complexity :worst : worst : O(UK),for number ; O(UCK),for characters
Space complexity : worst : O(UK),for number ; O(UCK),for characters
"""

import CountingSort


def radixSort(array, thetype):
    """
    argument :array - the list of list which contain userId and list of movie's id/movie's name
              thetype : number - sort the numbers in list of list
                        character - sort the characters in list of list
    return : output - the sorted list of list 
    """
    maxLength = findMaxLength(array)
    position = -1
    output = array[:]
    while position >= -maxLength:
        output = CountingSort.countingSort(output, position, thetype)
        position -= 1
    return output

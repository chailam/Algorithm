"""
Author: Loi Chai Lam
Date: 28 May 2024

Counting Sort
Use Counting sort to sort the list of characters or numbers.
A non-comparison-based sorting algorithm that works well when there is limited range of input values.
The basic idea behind Counting Sort is to count the frequency of each distinct element in the input array 
and use that information to place the elements in their correct sorted positions.

Complexity:
U –total numbers of item to be sorted, C - maximum number of characters in any item, 
K - maximum number of subitems in the item
Time complexity :worst : O(U)orU(K),for number ; O(UK),for characters
Space complexity : worst : O(UK),for number ; O(UCK),for characters
"""


def countingSort(array, position, thetype):
    """
    argument :array - the list of list which contain userId and list of movie's id/movie's name
              thetype : number - sort the numbers in list of list
                        character - sort the characters in list of list
                        position - the position of the character/number to be sorted
    return : output - the sorted list
    """
    output = []
    count = []
    tmp = getColumn(array, position)
    maximum = findMaxInList(tmp, thetype)
    for i in range(maximum + 1):
        count.append([])
    if thetype == "number":
        for i in range(len(array)):
            if (position + len(array[i][1])) >= 0:
                index = array[i][1][position]
                count[index].append(array[i])
            else:
                count[0].append(array[i])
    elif thetype == "character":
        for i in range(len(array)):
            if (position + len(array[i][1])) >= 0:
                index = ord(array[i][1][position])
                count[index].append(array[i])
            else:
                count[0].append(array[i])
    for i in range(len(count)):
        numOccur = len(count[i])
        for j in range(numOccur):
            output.append(count[i][j])
    return output

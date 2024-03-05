''' 
Quick Select Algorithm
Author: Loi Chai Lam
Modified: 5 Mar 2024

Quick Select is the improvement of quick sort.
It is to find the k-th smallest element in an unordered list.

The algorithm is similar to QuickSort. The difference is, instead of recurring for both sides (after finding pivot), 
it recurs only for the part that contains the k-th smallest element. 
The logic is simple, 
if index of the partitioned element is more than k, then we recur for the left part. 
If index is the same as k, we have found the k-th smallest element and we return. 

Best-case complexity: O(N)
Worst-case complexity: O(N^2)
'''
import numpy


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def partition(array, start, end):
    # find the middle index of the array and set that as pivot
    mid = (start + end) // 2
    pivot = array[mid]
    # swap the pivot to the leftmost
    swap(array, start, mid)
    # partition the list into two parts where
    # value smaller than pivot should be in left
    # and larger than pivot should be in right
    index = start
    for k in range(start+1, end+1):
        if array[k] < pivot:
            index += 1
            swap(array, k, index)
    swap(array, start, index)
    # return the index of the pivot
    return index


def quick_select(array, k):
    '''
    k: the k-th smallest number in array to be found
    array: thr array to sort
    '''
    start = 0
    end = len(array)-1
    indexPivot = partition(array, start, end)
    while indexPivot != (k - 1):
        # if the pivot index less than the k-position, partition the right side
        if indexPivot < k - 1:
            indexPivot = partition(array, indexPivot+1, end)
            # if the pivot index larger than the k-position, partition the left side
        elif indexPivot > k - 1:
            indexPivot = partition(array, start, indexPivot)
        else:
            # if the pivot index equal to the k-position, return the value
            break
    return array[indexPivot]


arr = [55, 94, 69, 11, 66, 99, 22]
k = len(arr)//2
assert k <= len(arr), "k should be less than length of the array"
print("The smallest ", k, "-th value in", arr, "is", quick_select(arr, k))

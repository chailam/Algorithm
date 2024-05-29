''' 
Quick Sort Modified Version to use Quick Select Algorithm
Author: Loi Chai Lam
Modified: 5 Mar 2024

!!! Need to be further improved, too much recursive!!!


Modified version of the Quick Sort algorithm such that it does
not choose the first element as pivot. Instead, call the Quick Select
algorithm to find the median and choose it as
the pivot.
'''

'''
============================Quick Select========================================
'''


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


'''
============================Quick Sort using Quick Select to choose Median========================================
'''


def partition_qs(array, start, end):
    mid = len(array) // 2
    pivot = quick_select(array, mid)
    return mid


def quick_sort(array):
    start = 0
    end = len(array)-1
    quick_sort_aux(array, start, end)


def quick_sort_aux(array, start, end):
    if start < end:
        mid = partition_qs(array, start, end)
        quick_sort_aux(array, start, mid-1)
        quick_sort_aux(array, mid+1, end)


arr = [55, 94, 69, 11, 66, 99, 22]
quick_sort(arr)

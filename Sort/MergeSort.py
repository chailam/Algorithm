# Merge Sort

def mergeLists(lefthalf, righthalf, merged):
    merged.clear() # clear the list (in case not already empty)
    i,j =0,0 # initialize i and j to zero
    # repeat until reaches end of at least one list
    while i < len(lefthalf) and j < len(righthalf):
         # add the smaller element to list and increment its pointer
         if lefthalf[i] < righthalf[j]:
             merged.append(lefthalf[i])
             i=i+1
         else:
             merged.append(righthalf[j])
             j=j+1
    # add the remaining elements of the unfinished list in merged
    if i < len(lefthalf):
        merged += lefthalf[i:]
    if j < len(righthalf):
        merged += righthalf[j:]


def mergeSort(alist):
    # divide the list into two halves
    mid = len(alist)//2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]
    # recursively sort each half if it contains more than 1 elements
    if len(lefthalf) > 1:
        mergeSort(lefthalf)
    if len(righthalf) > 1:
        mergeSort(righthalf)
    # at this point, both halves have been recursively sorted
    # merge the two halves into the alist
    mergeLists(lefthalf,righthalf,alist)
    print(alist)

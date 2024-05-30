''' 
QuickSort Algorithm
Author: Loi Chai Lam

Best-case Height: O(logN)
Best-case complexity: O(N logN)

Worst-case Height: O(N)
Worst-case complexity: O(N^2)


'''


def partition(alist, first, last):
    pivot = alist[first]
    LBAD = first+1
    RBAD = last-1
    # continue until pointers cross
    while LBAD <= RBAD:
        # move LBAD until it points to a bad element or crosses RBAD
        # !!!还要写 LBAD <= RBAD因为之前他达到了目标,但是过后LBAD加进去的话就没达到了..所以要写
        while LBAD <= RBAD and alist[LBAD] <= pivot:
            LBAD = LBAD + 1
        # move RBAD until it points to a bad element or crosses LBAD
        while LBAD <= RBAD and alist[RBAD] > pivot:
            RBAD = RBAD - 1
        # only swap if they have not crossed
        if LBAD <= RBAD:
            # Python shorthand for swapping
            alist[LBAD], alist[RBAD] = alist[RBAD], alist[LBAD]
    # if they have crossed, swap element at RBAD with element at pivot
    alist[first], alist[RBAD] = alist[RBAD], alist[first]
    return RBAD  # return pivot position at after partitioning


def quickSort(alist, first, last):
    # we need to sort only if the list contains at least two elements
    if (last - first) > 1:
        # partition the list from first to last (exclusive)
        # print("partitioning", alist[first:last], "pivot",alist[first])
        pivot_pos = partition(alist, first, last)
        # print("partitioned:", alist[first:last])

        # recursively sort the two halves of the list
        # print("Splitting into two", alist[first:pivot_pos],alist[pivot_pos+1:last])
        quickSort(alist, first, pivot_pos)
        quickSort(alist, pivot_pos+1, last)


alist = ['Newport', 'South Kingsville', 'Spotswood', 'Williamstown', 'Altona',
         'Seaholme', 'Braybrook', 'Robinson', 'Albanvale', 'Kealba', 'Kings Park', 'St Albans']
quickSort(alist, 0, len(alist))
print(alist)

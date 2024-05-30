"""
Author: Loi Chai Lam
Date: 10 Mar 2017

Partial Heap Sort
This sorting algorithm is to ue heap to do a partial heap sort
with the given list and gven top-k elements.

The python file read the data from a input file and perform a partial heal sort for the data.
Each line in the file has two values separated by a colon :. The first value is the Index Number and
the second value is the value to be sorted. Below are the first 5 lines from the file.
    1:9695819
    2:5004755
    3:611496
    4:2006676
    5:42359

Complexity:
Best : O(N), where N is length of the list
Worst : O(Nlogk),where k is top-k and N is length of the list

"""
# import required module


import sys  # nopep8
import os  # nopep8

# append the path of the parent directory
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'DataStructure'))  # nopep8

from min_heap import Heap


def partialHeapSort(alist, k):
    """
    argument : alist : the list needed to be partial heap sort
                k : the top-k elements need
    return : tmp : top-k elements of the list in descending order

    """
    pHS = Heap(k)
    for i in range(len(alist)):
        pHS.add(alist[i])
    tmp = [None] * k
    for i in range(k - 1, -1, -1):
        tmp[i] = pHS.get_min()
    return tmp


def printResult(alist):
    """
    To print the result in the given format
    complexity: best : O(N), where N is length of the list
                worst : O(N), where N is length of the list
    argument : alist : the sorted list
    return : -

    """
    for i in range(len(alist)):
        print("#" + str(i + 1) + " : Index Number : " + str(alist[i][0]) + " Time spent : " + str(alist[i][1]))


if __name__ == "__main__":

    """
    To read the file into an array, complexity os O(N),
    where N is the number of users
    """
    filename = "./SampleData/partialHeapSortSampleData.txt"
    array = []
    file = open(filename, "r", encoding="UTF-8-sig")
    for line in file:
        line = line.strip("\n")
        line = line.split(":")
        array.append((int(line[0]), int(line[1])))
    file.close()

    k = int(input("Enter the value of k : "))
    result = partialHeapSort(array, k)
    printResult(result)

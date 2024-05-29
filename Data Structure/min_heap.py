"""
Author: Loi Chai Lam
Date: 28 May 2024

Min Heap
A type of Heap Data Structure in which each node is smaller than or equal to its children. 
The value in this min heap is a 2D array where first value is the index of the number and second value is the number itself.

This is used with the PartialHeapSort.py under the Sorting Algorithm.

"""

from referential_array import build_array


class Heap:
    """
    The class, Heap is using the array to implement the heap.
    A min_heap

    """

    def __init__(self, k):
        """
        The initialise method in the list
        complexity: best : O(1)
                    worst : O(1)
        argument : k : the size of the heap
        return : -

        """
        self.count = 0
        self.limit = k + 1
        self.array = build_array(self.limit)

    def swap(self, i, j):
        """
        Swap two elements in the array
        complexity: best : O(1) 
                    worst : O(1)
        argument : i : index of first element
                    j : index of second element
        return : -        
        """
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def rise(self, i):
        """
        To rise the number to maintain the min-heap invariant
        If the number is smaller than its parent, it will swap the
        position with its parent
        complexity: best : O(1) 
                    worst : O(logk),where k is the length of the array(fixed)
        argument : i : the index of the number
        return : -

        """
        while i > 1 and self.array[i][1] < self.array[i // 2][1]:
            self.swap(i, i // 2)
            i = i // 2

    def sink(self, i):
        """
        To sink the number to maintain the min-heap invariant
        If the number is larger than its smallest child, it will swap the
        position with its smallest child
        To maintain the stability, if the number is same as the number of its
        smallest child, it will check for the index of the number.
        Only the larger index will become the parent
        complexity: best : O(1) 
                    worst : O(logk),where k is the length of the array(fixed)
        argument : i : the index of the number
        return : -

        """
        while 2 * i <= self.count:
            child = self.smallest_child(i)
            if self.array[i][1] > self.array[child][1]:
                self.swap(child, i)
                i = child
            elif self.array[i][1] == self.array[child][1]:
                if self.array[i][0] > self.array[child][0]:
                    break
                self.swap(child, i)
                i = child
            else:
                break

    def smallest_child(self, i):
        """
        To get the smallest child of the parent
        complexity: best : O(1) 
                    worst :  O(1)
        argument : i : the index of the parent
        return : 2*1(left child) : if left child is smaller than right child
                (2*i)+1(right child) : if right child is smaller than left child or
                if value of left child and right child are same but the index of
                left child is larger than right child

        """
        if 2 * i == self.count or self.array[2 * i][1] < self.array[(2 * i) + 1][1]:
            return 2 * i
        elif self.array[2 * i][1] == self.array[(2 * i) + 1][1]:
            if self.array[2 * i][0] > self.array[(2 * i) + 1][0]:
                return 2 * i
            return (2 * i) + 1
        else:
            return (2 * i) + 1

    def add(self, item):
        """
        To add the number(tuple) into the min_heap
        If the heap is not full, just add it at the end and rise it
        If the heap is full and the item is larger than the heap, remove the
        min(first element in array) and sink it
        complexity: best : O(1) 
                    worst : O(logk),where k is the length of the array(fixed)
        argument : item : the item to be added
        return : -

        """
        if self.count + 1 < self.limit:
            self.array[self.count + 1] = item
            self.count += 1
            self.rise(self.count)
        else:
            if item[1] > self.array[1][1]:
                self.array[1] = item
                self.sink(1)

    def get_min(self):
        """
        To get the minimum number in the array(the first element)
        complexity: best : O(1) 
                    worst : O(logk),where k is the length of the array(fixed)
        argument : -
        return : item : the minimum item

        """
        item = self.array[1]
        self.swap(1, self.count)
        self.count -= 1
        self.sink(1)
        return item




if __name__ == "__main__":
    pass

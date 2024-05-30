"""
Author: Loi Chai Lam
Date: 14 May 2018

The modified min heap used to implement the Dijkstra algorithm.
It includes the array of vertices in the Heap to store the Vertex class for Dijkstra algorithm.

"""
# Min Heap
from referential_array import build_array


class MinHeap:
    """
    The class,Heap is using the array to implement the heap.
    A min_heap

    """

    def __init__(self, numVertex):
        """
        The initialise method in the list
        complexity: best : O(1)
                    worst : O(1)
        argument :-
        return : -

        """
        self.count = 0
        self.array = build_array(100)
        self.vertices = [-2 for i in range(numVertex)]

    def _resize(self):
        new_array = build_array(2 * len(self.array))
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array


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
            self.vertices[self.array[i][0].vertex] = i
            self.vertices[self.array[i // 2][0].vertex] = i // 2
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
                self.vertices[self.array[i][0].vertex] = i
                self.vertices[self.array[child][0].vertex] = child
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
        if self.count + 1 < len(self.array):
            self.array[self.count + 1] = item
        else:
            self._resize()
            self.array[self.count + 1] = item
        self.count += 1
        self.vertices[int(item[0].vertex)] = self.count
        self.rise(self.count)


    def get_min(self):
        """
        To get the minimum number in the array(the first element)
        complexity: best : O(1) 
                    worst : O(logk),where k is the length of the array(fixed)
        argument : -
        return : item : the minimum item

        """
        item = self.array[1]
        self.vertices[int(item[0].vertex)] = -1  # finalized
        self.swap(1, self.count)
        self.count -= 1
        self.sink(1)
        return item

    def empty(self):
        """
        To check whether the minheap is empty
        complexity: best : O(1) 
                    worst : O(1)
        argument : -
        return : true if it is empty ; false otherwise

        """
        return self.count == 0

    def __str__(self):
        string = ""
        for i in range(1, self.count + 1):
            string += str(self.array[i])
        return string

    def update_min(self, item):
        """
        time: O(logV), V is numVertex
        space:O(V)
        """
        position = self.vertices[int(item[0].vertex)]
        self.array[position] = item
        self.rise(position)


if __name__ == "__main__":
    a = MinHeap(13)  # 6105+1
    a.add([12, 4])
# a.add([8,14])
# a.add([3,18])
# a.add([5,11])
# a.add([10,15])
# a.add([2,9])
# a.add([11,13])
# a.update_min([5,3])
# a.update_min([5,1])
# a.get_min()
    # a.get_min()
    print(a.vertices)
    print(a)

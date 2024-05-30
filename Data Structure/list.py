"""
Author: Loi Chai Lam
Date: 30 May 2024
Assignment 2 Task 2

List Data Structure

The base size of the array is 20 and should never be less than 20. 
However, if the list becomes full, it is resized to be 2 times
larger than the current size. 

Likewise, the underlying size should  decrease by half if the underlying array 
is larger than the base size but the content occupies less than 1/8 of the 
available space. When resizing the list, retain the contents of the list. 

That is, when it is initially filled, it will be resized to 20 items, then 40,
while retaining the contents initially in it. The same happens when the size of the array shrinks.

"""
from referential_array import build_array


class List:
    """
    The class,List is using the array to implement the list.
    The array is given and is imported.

    """

    def __init__(self):
        """
        The initialise method in the list
        precondition : -
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : -
        return : -

        """
        self.size = 20
        self.array = build_array(self.size)
        self.count = 0

    def __len__(self):
        """
        The builtin method, called by len(self)
        precondition : -
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : -
        return : the length of the list, which is self.count

        """
        return self.count

    def __str__(self):
        """
        The builtin method, called by str(self)
        precondition : -
        postcondition : -
        complexity: best : O(N) ,N is the length of the list  
                    worst : O(N),N is the length of the list 
        argument : -
        return : string representation of the list, which one item per line

        """
        string = ""
        for i in range(len(self) - 1):
            string += str(self[i]) + "\n"
        if len(self) > 0:
            string += str(self[len(self) - 1])
        return string

    def __contains__(self, item):
        """
        The builtin method in the list, called by item in self
        precondition : -
        postcondition : -
        complexity: best : O(1), if list[0] is the item which need to find 
                    worst : O(N) ,N is the length of the list , if item not in the list
        argument : item : the item which need to check
        return : True if item is in the list, False otherwise

        """
        for i in range(len(self)):
            if item == self[i]:
                return True
        return False

    def valid_index(self, index):
        """
        To check the validity of the index
        precondition : -
        postcondition : -
        complexity: best : O(1) 
                    worst : O(1)
        argument : index : the index need to be checked
        return : True if is valid index, False otherwise

        """
        return index < len(self) and index >= -len(self)

    def __getitem__(self, index):
        """
        The builtin method in the list, called by self[index], it returns the index in the list
        precondition : the index must be a valid index
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : index : the required index in the list
        return : returns the item at index in the list, if index is non-negative.
                 If it is negative, it will return the last item if index is −1, the second-to last if index is −2,
                 and so on up to minus the length of the list, which returns the first item

        """
        if not self.valid_index(index):
            raise IndexError("Invalid Index")
        if index >= 0:
            return self.array[index]
        else:
            return self.array[len(self) + index]

    def __setitem__(self, index, item):
        """
        The builtin method in the list, called by self[index] = item, sets the value at index in the list to be item
        precondition : the index must be a valid index
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : index : the required index in the list
                   item : the required item which need to set
        return : -

        """
        if not (index <= len(self) and index >= -len(self)):
            raise IndexError("Invalid Index")
        if index >= 0:
            self.array[index] = item
        else:
            self.array[len(self) + index] = item

    def __eq__(self, other):
        """
        The builtin method in the list, called by self == other
        precondition : the index must be a valid index
        postcondition : -
        complexity: best : O(1) ,if the length of the array not equal to the other or if the self.array[0] != other[0]
                    worst : O(N) ,N is the length of the list , if all items are same

        argument : other : other list to be compared
        return : True if this list is equivalent to other

        """
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def modify_size(self):
        """
        Modify the size of the list when it become full,
        shrink when the content occupies less than 1/8 of the available space
        precondition : base size of array is 20
        postcondition : -
        complexity: best : O(N) ,N is the length of the list 
                    worst : O(N) ,N is the length of the list 

        argument : -
        return : -

        """
        if len(self) >= self.size:
            self.size = self.size * 2
            self.array_modified = build_array(self.size)
            for i in range(len(self)):
                self.array_modified[i] = self.array[i]
            self.array = self.array_modified
        elif self.size > 20 and len(self) <= self.size * (1 / 8):
            self.size = self.size // 2
            self.array_modified = build_array(self.size)
            for i in range(len(self)):
                self.array_modified[i] = self.array[i]
            self.array = self.array_modified

    def append(self, item):
        """
        Adds item to the end of the list
        precondition : -
        postcondition : -
        complexity: best : O(1), if the list is not full or not the length of the list <= (1/8)*size of the array
                    worst : O(N), N is the length of the list, if the list is full or is too small, need to reimplement
        argument : item : the item need to be added
        return : -

        """
        self.modify_size()
        self[self.count] = item
        self.count += 1

    def insert(self, index, item):
        """
        Inserts item into self before position index
        precondition : the index must be a valid index
        postcondition : -
        complexity: best :  O(N), N is the length of the list
                    worst : O(N) ,N is the length of the list
        argument : item : the item need to be inserted
                   index : the index of the item need to be inserted
        return : -

        """
        self.modify_size()
        if index < 0:
            index = len(self) + index
        for i in range(len(self) - 1, index - 1, -1):
            self[i + 1] = self[i]
        self[index] = item
        self.count += 1

    def delete(self, index):
        """
        Deletes the item at index from the list,
        moving all items after it towards the start of the list
        precondition : the index must be a valid index
        postcondition : -
        complexity: best : O(N), N is the length of the list
                    worst : O(N), N is the length of the list
        argument : index : the index of the item need to be deleted
        return : -

        """
        self.modify_size()
        if not self.valid_index(index):
            raise IndexError("Invalid Index")
        if index < 0:
            index = len(self) + index
        for i in range(index, len(self) - 1):
            self[i] = self[i + 1]
        self.count -= 1

    def remove(self, item):
        """
        Deletes the first instance of item from the list
        precondition : the item must exist in the list
        postcondition : -
        complexity: best : O(1) ,if the item is at list[0] and the list is not full or too small
                    worst : O(N), N is the length of the list, if the index of the item is the last index 
        argument : item : the item in the first instance need to be deleted
        return : -

        """
        self.modify_size()
        if not (item in self):
            raise ValueError("Item does not exist")
        for i in range(len(self)):
            if item == self[i]:
                self.delete(i)
                break

    def sort(self, reverse):
        """
        Sorts the items in the list using bubble sort
        precondition : -
        postcondition : -
        complexity: best : O(N) ,N is the length of the list, if the list is sorted
                    worst : O(N**2), N is the length of the list, if the list is not sorted and it needs to loop twice
        argument : reverse : if reverse is False, sort the list in ascending order
                             if reverse is True, sort the list in descending order
        return : -

        """
        for i in range(len(self) - 1):
            swapped = False
            for j in range(len(self) - 1 - i):
                if reverse == False:
                    if self[j] > self[j + 1]:
                        self[j], self[j + 1] = self[j + 1], self[j]
                        swapped = True
                elif reverse == True:
                    if self[j] < self[j + 1]:
                        self[j], self[j + 1] = self[j + 1], self[j]
                        swapped = True
            if not swapped:
                break


if __name__ == "__main__":
    list1 = List()
    for i in range(75):
        list1.append(1)
    print(list1.size)
    print(len(list1))
    print()

    for i in range(66):
        list1.remove(1)
    for i in range(6):
        list1.remove(1)
    print(list1)
    print(list1.size)
    print(len(list1))

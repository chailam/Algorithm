"""
author : Loi Chai Lam
date : 27 Sep 2017
title : Assignment 3 Task 1 (Hash Table with Linear Probing)


Hash Table with Linear Probing
Data Structure for Hash Table.
In case of collision, it will use the Linear Probing Collision Handling technique,
an Open Addressing Collision Handling method.

In linear probing, the hash table is searched sequentially that starts from 
the original location of the hash. If in case the location that we get is already occupied, 
then we check for the next location.
"""

from referential_array import build_array
import timeit



class HashTableLinear():
    """
    The class,HashTableLinear is using the array and linear probing to implement the Hash Table.
    The array is given and is imported.

    """

    def __init__(self, a=101, size=7919):
        """
        The initialise method in the list
        precondition : -
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : a : the base, default is 101
                   size : the table size, default is 7919
        return : -

        """
        self.table_size = size
        self.count = 0
        self.a = a
        self.array = build_array(self.table_size)
        self.probe = 0
        self.collision = 0


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


    def __getitem__(self, key):
        """
        The builtin method, called by table[key],
        it returns the value corresponding to key in the hash table
        precondition : -
        postcondition : -
        complexity: best : O(1), if the key is in its first own position
                    worst : O(N), N is table_size, if the key is the last item in the table_size
        argument : key : the key of the hash value
        return : the value of the key

        """
        position = self.hash_value(key)
        for _ in range(self.table_size):
            if self.array[position] is None:
                raise KeyError("Key Not Found")
            elif self.array[position][0] == key:
                return self.array[position][1]
            else:
                position = (position + 1) % self.table_size
        raise KeyError("Key Not Found")


    def __setitem__(self, key, value):
        """
        The builtin method, called by table[key] = value,
        sets the value corresponding to key in the hash table to be value
        precondition : -
        postcondition : -
        complexity: best : O(1), if the first position is None, or equal to key 
                    worst : O(N), N is table_size, if the table is full and the key is a new key
        argument : key : the key of the hash value
                   value : the value of the hash value
        return : -

        """
        position = self.hash_value(key)
        if self.array[position] is not None:
            if self.array[position][0] != key:
                self.collision += 1
        for _ in range(self.table_size):
            if self.array[position] is None:
                self.array[position] = (key, value)
                self.count += 1
                return
            elif self.array[position][0] == key:
                self.array[position] = (key, value)
                return
            else:
                self.probe += 1
                position = (position + 1) % self.table_size
        raise Exception("Hash Table Full")



    def __contains__(self, key):
        """
        The builtin method, called by key in table
        precondition : -
        postcondition : -
        complexity: best : O(1),if the first position is the key 
                    worst : O(N) ,N is table_size , if key not in the table
        argument : key : the key of the hash value
        return : True if item is in the table, False otherwise

        """
        position = self.hash_value(key)
        for _ in range(self.table_size):
            if self.array[position] is None:
                return False
            elif self.array[position][0] == key:
                return True
            else:
                position = (position + 1) % self.table_size
        return False


    def __str__(self):
        """
        The builtin method, called by str(self)
        precondition : -
        postcondition : -
        complexity: best : O(N) ,N is the length of the array  
                    worst : O(N),N is the length of the array
        argument : -
        return : output :  representation of the array

        """
        output = ""
        for item in self.array:
            if item is not None:
                (key, value) = item
                output += "(" + str(key) + ", " + str(value) + ")"
        return output


    def hash_value(self, key):
        """
        Calculate the hash value for the given key.
        precondition : -
        postcondition : -
        complexity: best : O(N), N is the length of the key
                    worst : O(N), N is the length of the key
        argument : key : the key need to calculate the value
        return : h : the position of the key in the array

        """
        h = 0
        for c in key:
            h = (h * self.a + ord(c)) % self.table_size
        return h


def read1(filename, a, size):
    """
    Takes a filename and size as input and reads the words in it into the hash table
    precondition : filename must exist
    postcondition : -
    complexity : best : O(N), N is the length of the file
                 worst : O(N), N is the length of the file
    argument : filename : the name of the file
               size : the table size
               a : the base
    return : taken : the time taken to read the words into the hash table
             aveProbe : the average probe length
             collision : the number of collisions

    """
    myHash = HashTableLinear(a, size)
    file = open(filename, "r", encoding="UTF-8-sig")
    start = timeit.default_timer()
    for line in file:
        line = line.strip("\n")
        myHash[str(line)] = str(line)
    taken = (timeit.default_timer() - start)
    aveProbe = myHash.probe / len(myHash)
    collision = myHash.collision
    file.close()
    return taken, aveProbe, collision



if __name__ == "__main__":

    table_size = [210000, 209987, 400000, 399989, 202361]
    a = [101, 565427, 2001, 3217, 151]

# this input file is just sample data with lines of items to be inserted into the hash table
    filename = "english_small.txt"
    print(filename)
    for i in range(len(table_size)):
        for j in range(len(a)):
            result = read1(filename, a[j], table_size[i])
            print("table_size:", table_size[i], "a:", a[j])
            print("wallTime:%.2f" % result[0], "averageProbe:%.2f" % result[1], "collision:%.2f" % result[2])



"""
a = 151 table_size = 399989
Based on the result, the table_size of 399989 is the best as the maximum table size
is 400000, since the table size should be prime number (if not prime, will share
common factor and cause collision), hence, the sutable table size is 399989. The best a is 151
from the result as 151 also a prime number
"""

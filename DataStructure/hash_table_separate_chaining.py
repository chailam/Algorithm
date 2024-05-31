"""
author : Loi Chai Lam
date : 28 Sep 2017
title : Assignment 3 Task 4 (Hash Table with Separate Chaining)


Hash Table with Separate Chaining
Data Structure for Hash Table.
In case of collision, it will use the Separate Chaining Collision Handling technique.

The linked list data structure is used to implement this technique. 
When multiple elements are hashed into the same slot index, then these elements are inserted 
 a singly-linked list which is known as a chain.  

"""

from linked_list import LinkedList
from referential_array import build_array
import timeit
from node import Node




class HashTableSeparateChaining():
    """
    The class,HashTableSeparateChaining is using the linked list to implement the Hash Table.

    """

    def __init__(self, a=151, size=399989):
        """
        The initialise method in the list
        precondition : -
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : a : the base
                   size : the table size
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
        complexity: best : O(1), if the key is in its first position in chain
                    worst : O(N), N is length of the chain, if the key is not found
                    argument : key : the key of the hash value
        return : the value of the key

        """
        position = self.hash_value(key)
        if self.array[position] is None:
            raise KeyError("Key Not Found")
        else:
            chain = self.array[position]
            for i in range(len(chain)):
                if chain[i][0] == key:
                    return chain[i][1]
        raise KeyError("Key Not Found")


    def __setitem__(self, key, value):
        """
        The builtin method, called by table[key] = value,
        sets the value corresponding to key in the hash table to be value
        precondition : -
        postcondition : -
        complexity: best : O(1), if the first position is None, or equal to key 
                    worst : O(N), N is length of the chain, if the key is a new key and has a collusion
        argument : key : the key of the hash value
                   value : the value of the hash value
        return : -

        """
        position = self.hash_value(key)
        if self.array[position] is not None:
            self.collision += 1
        if self.array[position] is None:
            chain = LinkedList()
            chain.append((key, value))
            self.array[position] = chain
            self.count += 1
            return
        else:
            chain = self.array[position]
            for i in range(len(chain)):
                if chain[i][0] == key:
                    chain[i] = (key, value)
                    return
                self.probe += 1
            chain.append((key, value))
            self.count += 1
            return

    def __contains__(self, key):
        """
        The builtin method, called by key in table
        precondition : -
        postcondition : -
        complexity: best : O(1), if the position is none
                    worst : O(N) ,N is length of the chain , if key not in the chain
        argument : key : the key of the hash value
        return : True if item is in the table, False otherwise

        """
        position = self.hash_value(key)
        if self.array[position] is None:
            return False
        else:
            chain = self.array[position]
            for i in range(len(chain)):
                if chain[i][0] == key:
                    return True
            return False



    def __str__(self):
        """
        The builtin method, called by str(self)
        precondition : -
        postcondition : -
        complexity: best : O(N**2) ,N is the length of the array  
                    worst : O(N),N is the length of the array
        argument : -
        return : output :  representation of the array

        """
        output = ""
        for item in self.array:
            if item is not None:
                for i in range(len(item)):
                    output += "(" + str(item[i][0]) + ", " + str(item[i][1]) + ")"
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


def read(filename, a, size):
    """
    Takes a filename and size as input and reads the words in it into the hash table
    precondition : filename must exist
    postcondition : -
    complexity : best : O(N), N is the length of the file
                 worst : O(N), N is the length of the file
    argument : filename : the name of the file
               size : the table size
    return : taken : the time taken to read the words into the hash table
             aveProbe : the average probe length
             numCollision : the number of collisions

    """
    myHash = HashTableSeparateChaining(a, size)
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
    a = 151
    table_size = 399989

# this input file is just sample data with lines of items to be inserted into the hash table
    filename = "english_small.txt"
    print(filename)
    print("table_size:", table_size, "a:", a)
    print("Separate Chaining")
    result = read(filename, a, table_size)
    print("wallTime:%.2f" % result[0], "averageProbe:%.2f" % result[1], "collision:%.2f" % result[2])

"""
For 3 files, the average probe and number of collisions in separate chaining
is smaller than linear probing.
However, the wallTime in separate chaining is larger than linea probing.

"""

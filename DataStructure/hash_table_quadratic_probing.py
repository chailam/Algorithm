"""
author : Loi Chai Lam
date : 28 Sep 2017
title : Assignment 3 Task 4 (Hash Table with Quadratic Probing)


Hash Table with Quadratic Probing
Data Structure for Hash Table.
In case of collision, it will use the Quadratic Probing Collision Handling technique, 
an Open Addressing Collision Handling method.

Quadratic probing is an open-addressing scheme where we look for the i‘th slot in 
the i’th iteration if the given hash value x collides in the hash table. 

The has is implemented using  dynamic hashing, by doubling the size of the underlying array (and rehashing) every time
the load exceeds 2/3
"""

from referential_array import build_array
import timeit


class HashTableQuadratic():
    """
    The class,HashTableQuadratic is using the array and linear probing to implement the Hash Table.
    The array is given and is imported.

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

    def modify_size(self):
        """
        Doubling the size of the underlying array(and rehashing) every time the load exceeds 2/3
        precondition : -
        postcondition : -
        complexity: best : O(1), if the load factor !> 2/3
                    worst : O(N), N is the length of tmp_array, need to loop through to rehash
        argument : -
        return : -

        """
        load_factor = len(self) / self.table_size
        if load_factor > (2 / 3):
            tmp_array = self.array
            self.table_size = (self.table_size * 2) + 1
            self.array = build_array(self.table_size)
            self.count = 0
            for i in tmp_array:
                if i is not None:
                    self[i[0]] = i[1]

    def __getitem__(self, key):
        """
        The builtin method, called by table[key],
        it returns the value corresponding to key in the hash table
        precondition : -
        postcondition : -
        complexity: best : O(1), if the key is in its first own position
                    worst : O(N), N is table_size, if the key is not found and table is full
        argument : key : the key of the hash value
        return : the value of the key

        """
        position = self.hash_value(key)
        h = position
        i = 1
        for _ in range(self.table_size):
            if self.array[position] is None:
                raise KeyError("Key Not Found")
            elif self.array[position][0] == key:
                return self.array[position][1]
            else:
                position = (h + i**2) % self.table_size
                i += 1
        raise KeyError("Key Not Found")


    def __setitem__(self, key, value):
        """
        The builtin method, called by table[key] = value,
        sets the value corresponding to key in the hash table to be value
        precondition : -
        postcondition : -
        complexity: best : O(1), if the first position is None, or equal to key 
                    worst : O(N), N is table_size, if the key is a new key and i the probe length is high
        argument : key : the key of the hash value
                   value : the value of the hash value
        return : -

        """
        position = self.hash_value(key)
        h = position
        i = 1
        self.modify_size()
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
                position = (h + i**2) % self.table_size
                i += 1


    def __contains__(self, key):
        """
        The builtin method, called by key in table
        precondition : -
        postcondition : -
        complexity: best : O(1), if the first position is the key 
                    worst : O(N) ,N is table_size , if key not in the table
        argument : key : the key of the hash value
        return : True if item is in the table, False otherwise

        """
        i = 1
        position = self.hash_value(key)
        h = position
        for _ in range(self.table_size):
            if self.array[position] is None:
                return False
            elif self.array[position][0] == key:
                return True
            else:
                position = (h + i**2) % self.table_size
                i += 1
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


def read(filename, a, size):
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
             numCollision : the number of collisions

    """
    myHash = HashTableQuadratic(a, size)
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
    print("Quadratic")
    result = read(filename, a, table_size)
    print("wallTime:%.2f" % result[0], "averageProbe:%.2f" % result[1], "collision:%.2f" % result[2])

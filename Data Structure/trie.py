"""
Author: Loi Chai Lam
Date: 28 May 2024

Trie
Also called digital tree or prefix tree, is a type of k-ary search tree, 
a tree data structure used for locating specific keys from within a set. 
These keys are most often strings, with links between nodes defined not by the entire key, but by individual characters.
It is commonly used for efficient retrieval and storage of keys in a large dataset. 
The structure supports operations such as insertion, search, and deletion of keys, 

"""


class Node:
    """
    The class,Node used to create the node for Trie

    """

    def __init__(self):
        self.occurence = 0
        self.list = [None for i in range(27)]  # 27 is the length of alphabet
        self.character = ""


class Trie:
    def __init__(self):
        self.head = None
        self.current = None

    def insert(self, word):
        """
        Insert the data into the Trie in order to built the Trie
        argument : word: the key needed to be entered into the trie
        "$" recorded as end of the key
        return :-
        """
        if self.head == None:
            self.head = Node()
        self.current = self.head
        for i in word:
            self.current.occurence += 1
            self.current.character = i
            if self.current.list[ord(i) - ord('a')] is None:
                self.current.list[ord(i) - ord('a')] = Node()
            self.current = self.current.list[ord(i) - ord('a')]
        self.current.occurence += 1
        self.current.list[-1] = "$"


    def prefixSearch(self, prefix):
        """
        Get the prefix matched word and the number of words in the dictionary that have this prefix
        time complexity: worst : O(M+N),M is the length of prefix entered,
        N is total number of characters in the word 
        space complexity : worst : O(T)
        argument : prefix: the prefix entered by user needed to be searched
        return : False: if no such prefix;
                prefix+theStr: the word with highest frequency with that prefix
                theOccur: the number of words that have this prefixd
        """
        self.current = self.head
        for i in prefix:
            if self.current.list[ord(i) - ord('a')] is None:
                return False
            else:
                self.current = self.current.list[ord(i) - ord('a')]
        theStr = ""
        theOccur = self.current.occurence
        theCha = self.current.character
        theStr += theCha
        self.nextHigh = self.current.list[ord(theCha) - ord('a')]
        theStr += theCha
        return prefix + theStr, theOccur

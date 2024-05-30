"""
Author: Loi Chai Lam
Date: 28 Apr 2018

Word AutoComplete using Trie Data Structure
Assignment 3

Problem:

For a given prefix entered by the user, the program should:
1. Display the word with the highest frequency that matches the prefix.
2. Show the definition of the suggested word.
3. Indicate the total number of words with the given prefix.

For example, assume that the frequencies of “adversary”,
“advisory”, and “adventure” are 100, 200 and 150, respectively. If a user types “adv”, the modified
auto-complete system should display “advisory” with its definition and the number 43 that
corresponds to the number of words that have “adv” as a prefix . 



Requirement:
- The  program will have two components. 
First, you will construct a Trie. Then, for each of
the user’s entered prefix, you will need to return the relevant results. The worst-case time
complexity to construct the Trie must be O(T) where T is the total number of characters in
Dictionary file. The complexity requirements to return results for each of the user’s entered
prefix is O(M + N) where M is the length of the prefix entered by the user and N is the total
number of characters in the the word with the highest frequency and its definition. Note that
this is optimal because the size of the output string is O(M +N) and no algorithm can achieve
a better complexity. Note that N may be equal to M (i.e., the word is the same as the prefix
and the definition is empty). Also, note that, in this assignment, we are assuming that each
string comparison takes O(M) where M is the number of characters.




Input:
Input is the file contains around 3, 000 words, their frequencies and their
definitions. However, below we illustrate the input and output assuming that the
dictionary contains the details of only the following four words.

word: align
frequency: 358
definition: To adjust or form to a line; to range or form in line; to bring
into line; to aline.

word: adversary
frequency: 157
definition: One who is turned against another or others with a design to
oppose

word: advisory
frequency: 720
definition: Having power to advise; containing advice; as, an advisory
council; their opinion is merely advisory.

word: adventure
frequency: 696
definition: To try the chance; to take the risk.

You can assume that each word in the dictionary consists of only lowercase English letters 
(e.g., they do not contain white spaces, hyphens or other symbols).



Output:
The program must ask the user to enter a prefix. It must then
display the word with the highest frequency, its definition and the number of words that have
the input text as the prefix. 

If there are more than one words with the highest frequency, you
must display the alphabetically smallest word (e.g., if prefix is “be”, and “best” and “beast”
both have the same frequency (and highest among all words matching the prefix), your program
must display “beast” because it is alphabetically smaller than “best”). 

The program must keep asking the user to enter another prefix and terminate only when the user enters *** instead of
the prefix. 

Below is a sample execution of the program for the small data shown in the Input section above:

Enter a prefix: adv
Auto-complete suggestion: advisory
Definition: Having power to advise; containing advice; as, an advisory
council; their opinion is merely advisory.
There are 3 words in the dictionary that have "adv" as a prefix.

Enter a prefix: adve
Auto-complete suggestion: adventure
Definition: To try the chance; to take the risk.
There are 2 words in the dictionary that have "adve" as a prefix.

Enter a prefix:
Auto-complete suggestion: advisory
Definition: Having power to advise; containing advice; as, an advisory
council; their opinion is merely advisory.
There are 4 words in the dictionary that have "" as a prefix.

Enter a prefix: bat
There is no word in the dictionary that has "bat" as a prefix.

Enter a prefix: ***
Bye Alice!

Note that the third prefix entered by the user in the above example is an empty string in
which case the most frequent word in the whole dictionary is returned.



Thought:
In this task, I use Trie to implement the auto-complete suggestion program. First, I pre-process
the input file. I read the txt file and group the data into three main arrays, word, freq, and
definition. The word, freq and definition array contains all the words, its frequency and its
definition of the file. The worst-case time and space complexity of pre-processing the data is
O(T) where T is the total number of characters in file as I need to process all characters and save
them.

Second, I construct the Trie using the class Trie and class Node. In class Node, there are 3
instance variables, frequency, occurrence and list. Instance variable frequency will save the
highest frequency of the character in that Node; occurrence will save the number of times the
Node been called; list will contains a list of 27 slots.

In class Trie, during method insert, I check whether the Node for that character does exist. If the
Node does exist, I move to that Node, also add the occurrence by one and check for the highest
frequency. If the Node does not exist, I create a new class Node. I keep repeating these steps for
the length of the character times. The worst-case time complexity of inserting the word into the
Trie is O(N), where N is the length of the single word. The worst-case space complexity of the
method insert is O(T) where T is the total number of characters in input file.

In class Trie, the method prefixSearch, I first search for the prefix entered by the user. If the
prefix does not exist in the Trie, it will return False. If the prefix does exist in the Trie, I then
search for the character in the Trie that have the highest frequency of that prefix. If the highest
frequency of the next list and highest frequency of the current list are same, also if the
frequency of the endstring is also same as the highest frequency, I then return the string, its
frequency, the occurrence of that prefix and its definition. If either one is false, I keep going into
the next list with the highest frequency and repeat the checking process. The worst-case time
complexity of the prefixSearch method is O(M+N), where M is the length of the prefix and N is
the total number of characters in the word with highest frequency. The worst-case cpace
complexity for the method is O(T) where T is the total number of characters in input file.

"""


class Node:
    """
    The class,Node used to create the node for Trie

    """

    def __init__(self):
        self.frequency = [0, 0]
        self.occurence = 0
        self.list = [None for i in range(27)]


class Trie:
    def __init__(self):
        self.head = None
        self.current = None

    def insert(self, word, frequency, definition):
        """
        Insert the data into the Trie in order to built the Trie
        time complexity: worst : O(N),N is the length of a single word
        space complexity : worst : O(T),where T is the total number of characters
        argument : word: the word needed to be entered into the trie
                    frequency, definition: its frequency and definition
        return :-
        """
        if self.head == None:
            self.head = Node()
        self.current = self.head
        for i in word:
            self.current.occurence += 1
            if frequency > self.current.frequency[0]:
                self.current.frequency[0] = frequency
                self.current.frequency[1] = i
            elif frequency == self.current.frequency[0]:
                if ord(i) < ord(self.current.frequency[1]):
                    self.current.frequency[0] = frequency
                    self.current.frequency[1] = i
            if self.current.list[ord(i) - 97] is None:
                self.current.list[ord(i) - 97] = Node()
            self.current = self.current.list[ord(i) - 97]
        self.current.occurence += 1
        self.current.list[-1] = ("$", frequency, definition)

    def prefixSearch(self, prefix):
        """
        Get the prefix matched word having the highest frequency along with its definition
        and the number of words in the dictionary that have this prefix
        time complexity: worst : O(M+N),M is the length of prefix entered,
        N is total number of characters in the word with highest frequency and its definition
        space complexity : worst : O(T)
        argument : prefix: the prefix entered by user needed to be searched
        return : False: if no such prefix;
                prefix+theStr: the word with highest frequency with that prefix
                theFre: the frequency of the word
                theOccur: the number of words that have this prefix
                theDefinition: the definition of the word returned
        """
        self.current = self.head
        for i in prefix:
            if self.current.list[ord(i) - 97] is None:
                return False
            else:
                self.current = self.current.list[ord(i) - 97]
        theStr = ""
        theOccur = self.current.occurence
        theFre = self.current.frequency[0]
        theCha = self.current.frequency[1]
        self.nextHigh = self.current.list[ord(theCha) - 97]
        # if the prefix is the highest frequency
        if (self.current.list[-1] is not None and self.current.list[-1][1] == self.current.frequency[0]):
            return prefix + theStr, theFre, theOccur, self.current.list[-1][2]  # definition
        # elif prefix+next character is the highest frequency
        elif self.nextHigh.list[-1] is not None and self.nextHigh.list[-1][1] == self.current.frequency[0]:
            return prefix + theStr + theCha, theFre, theOccur, self.nextHigh.list[-1][2]  # definition
        else:
            while (self.nextHigh.frequency[0] == self.current.frequency[0]):
                self.current = self.nextHigh
                theStr += theCha
                theCha = self.current.frequency[1]
                self.nextHigh = self.current.list[ord(theCha) - 97]
            theStr += theCha
            return prefix + theStr, theFre, theOccur, self.nextHigh.list[-1][2]  # definition


def readFile(filename):
    """
    To read the file and separate it into list of list
    time complexity: worst : O(T),T is the total number of characters in file
    space complexity : worst : O(T)
    argument : filename : the filename which need to be read 
    return : word,freq,definition - the array containing the word,frequency,definition

    """

    word = []
    freq = []
    definition = []
    file = open(filename, "r", encoding="UTF-8-sig")
    number = 1
    for line in file:
        line = line.strip("\n")
        line = line.replace("word: ", "")
        line = line.replace("frequency: ", "")
        line = line.replace("definition: ", "")
        if number % 4 == 1:
            word.append(line)
        elif number % 4 == 2:
            freq.append(line)
        elif number % 4 == 3:
            definition.append(line)
        number += 1
    file.close()
    return word, freq, definition






if __name__ == "__main__":

    filename = "./Sample Data/wordAutocompleteSampleData.txt"
    wordList, freqList, definitionList = readFile(filename)
    trie = Trie()
    for i in range(len(wordList)):
        trie.insert(wordList[i], int(freqList[i]), definitionList[i])

    userInput = input("Enter a prefix: ")
    if userInput != "***":
        while userInput != "***":
            result = trie.prefixSearch(userInput)
            if result == False:
                print("There is no word in the dictionary that has " + userInput + " as a prefix.")
            else:
                print("Auto-complete suggestion: " + str(result[0]))
                print("Definition: " + str(result[3]))
                print("There are " + str(result[2]) + " words in the dictionary that have " + userInput + " as a prefix.")
            userInput = input("Enter a prefix: ")

    print("Bye Alice!")

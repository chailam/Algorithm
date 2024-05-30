"""
Author: Loi Chai Lam
Date: 16 Sep 2017
title : Assignment2 Task 4 (Editor using array-based List)

This program involves creating a simple line-oriented text editor in Python, 
similar to the early UNIX text editor "ed". The text editor will allow users 
to manipulate lines of text within a file using a variety of commands. The editor 
will be implemented using an array-based list data structure, enabling efficient access 
and modification of lines by their line numbers.


"""
import sys  # nopep8
import os  # nopep8

# append the path of the parent directory
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'DataStructure'))  # nopep8

from the_list import List


class Editor:
    """
    The class Editor using the class List to implement an editor

    """

    def __init__(self):
        """
        The initialise method in the editor
        precondition : -
        postcondition : -
        complexity: best : O(1)
                    worst : O(1)
        argument : -
        return : -

        """
        self.thelist = List()

    def read(self, filename):
        """
        Takes a filename as input and reads all the lines in from the file,
        put each as a separate item into a list
        precondition : filename must exist
        postcondition : -
        complexity: best :O(N), N is the length of the file
                    worst : O(N), N is the length of the file
        argument : filename : the filename which need to read
        return : self.thelist : the list in the editor appended

        """
        file = open(filename)
        for line in file:
            line = line.strip("\n")
            self.thelist.append(line)
        file.close()
        return self.thelist

    def write(self, filename):
        """
        Create or open a file, filename, writes every item in the list into the file
        precondition : -
        postcondition : a text file is created with name, filename
        complexity: best :O(N), N is the length of the list
                    worst   O(N), N is the length of the list
        argument : filename : the filename which need to write to
        return : -

        """
        file = open(filename, "w")
        for i in range(len(self.thelist) - 1):
            file.write(self.thelist[i])
            file.write("\n")
        if len(self.thelist) > 0:
            file.write(self.thelist[len(self.thelist) - 1])
        file.close()

    def search(self, word):
        """
        Takes a word and prints the line numbers in which the target word appears
        precondition : -
        postcondition : -
        complexity: best : O(N), N is the length of the list 
                    worst : O(N),N is the length of the list
        argument : word : the target word
        return : line_return : return the line numbers in list
                 False : if the item  ot in the list, return False

        """
        line_return = []
        word = word.lower()
        for i in range(len(self.thelist)):
            line = self.thelist[i].lower()
            if word in line:
                line_return.append(i)
        if len(line_return) == 0:
            return False
        else:
            return line_return

    def print(self, num1, num2):
        """
        Print the line in the list between position num1 and num2
        precondition : num1 < num2
        postcondition : -
        complexity: best : O(N),N is difference between num1 and num2 
                    worst : O(N),N is difference between num1 and num2 
        argument : num1 : the starting point of the item need to be printed
                   num2 : the ending point of the item need to be printed
        return : -

        """
        if num1 < 0:
            num1 = len(self.thelist) + num1
        if num2 < 0:
            num2 = len(self.thelist) + num2
        try:
            assert num1 < num2
            assert num2 < len(self.thelist)
            assert num1 >= 0
            for i in range(num1, num2 + 1, 1):
                print(self.thelist[i])
        except:
            print("?")

    def insert(self, num, text):
        """
        Inserts item into self before position index
        precondition : the index must be a valid index
        postcondition : -
        complexity: best :O(N) ,N is the length of the list
                    worst : O(N) ,N is the length of the list
        argument : text : the item need to be inserted
                   num : the index of the item need to be inserted
        return : -

        """
        self.thelist.insert(num, text)

    def delete_index(self, num):
        """
        Deletes the item at index from the list
        precondition : the index must be a valid index
        postcondition : -
        complexity: best : O(N), N is the length of the list
                    worst : O(N), N is the length of the list
        argument : num : the index of the item need to be deleted
        return : -

        """
        self.thelist.delete(num)

    def delete_all(self):
        """
        Deletes all item in the list
        precondition : -
        postcondition : -
        complexity: best : O(N), N is the length of the list
                    worst : O(N), N is the length of the list
        argument : -
        return : -

        """
        for i in range(len(self.thelist)):
            self.thelist.delete(0)

    def menu(self, command):
        """
        The menu of the Editor, it takes user's command and performs action
        precondition : -
        postcondition : -
        complexity: -
        argument : command : the user's command
        return : -

        """
        if command[0] == "print":
            try:
                assert len(command) == 3
                num1 = command[1]
                num2 = command[2]
                num1 = int(num1)
                num2 = int(num2)
                self.print(num1, num2)
            except:
                print("?")

        elif command[0] == "read":
            try:
                assert len(command) == 2
                filename = command[1]
                num = self.read(filename)
            except:
                print("?")

        elif command[0] == "write":
            try:
                assert len(command) == 2
                filename = command[1]
                self.write(filename)
            except:
                print("?")

        elif command[0] == "search":
            try:
                assert len(command) == 2
                word = command[1]
                the_return = self.search(word)
                if the_return == False:
                    print(False)
                else:
                    for i in the_return:
                        print(i)
            except:
                print("?")

        elif command[0] == "insert":
            try:
                assert len(command) == 2
                num = command[1]
                num = int(num)
                text = input("Enter the text need to insert : ")
                self.insert(num, text)
                self.stack.push(["insert", num])
            except:
                print("?")

        elif command[0] == "delete":
            try:
                assert len(command) == 1 or len(command) == 2
                if len(command) == 1:
                    stack_line = ["delete_all"]
                    for i in range(len(self.thelist)):
                        stack_line.append(self.thelist[i])
                    self.stack.push(stack_line)
                    self.delete_all()
                elif len(command) == 2:
                    num = command[1]
                    try:
                        num = int(num)
                    except:
                        print("?")
                    self.stack.push(["delete_index", self.thelist[num], num])
                    self.delete_index(num)
            except:
                print("?")

        elif command[0] == "undo":
            try:
                assert len(command) == 1
                pre_command = self.stack.pop()
                if pre_command[0] == "insert":
                    self.delete_index(pre_command[1])
                elif pre_command[0] == "delete_index":
                    self.insert(pre_command[2], pre_command[1])
                elif pre_command[0] == "delete_all":
                    for i in range(len(pre_command) - 1, 0, -1):
                        self.insert(0, pre_command[i])
            except:
                print("?")
        else:
            print("?")


if __name__ == "__main__":
    editor = Editor()
    while True:
        command = input()
        command = command.split(" ")
        if command[0] == "quit":
            break
        editor.menu(command)

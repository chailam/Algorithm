"""
Author: Loi Chai Lam
Date: 29 Mar 2018

Travelling Salesman Problem (TSP) using Dynamic Programming

Assignment 2a

Problem:
A door-to-door salesman is visiting a strange town where people really hate their neighbors.
He visited every house in the town and everyone told him that they are willing to buy some items from him 
but only if he does not sell anything to any of his neighbors. He noted down the items the residents 
of each house are willing to buy. Specifically, for each house (i), he has recorded the total price of the items (p_i),
residents of the house (i) will buy if he does not sell anything to any of the neighboring houses of (i). 
He need to maximizing his sales.



Neighbouring House Logic:
There are N houses along the street and are sequentially numbered 1 to N. A house numbered
i is called the neighboring house of a house j if |i − j| ≤ k where k is a value that the user
enters at the start of your program and |i − j| denotes the absolute difference between i and
j. k can be assumed will always be a positive integer smaller than or equal to N.
For example, if k = 3, the house number 50 is called the neighboring house of all the houses
numbered 47 to 53 and the house number 2 is the neighboring house of all the houses numbered
1 to 5. If k = 1, the house number 50 is the neighboring house of 49 and 51, and the house
number 2 is the neighboring house of 1 and 3.



Requirement:
- The solution must run in worst case O(N) time and use O(N) space.


Input:
The input file consists of 2 lines. The first line of the input is the value of N
corresponding to the total number of houses in the street. The next line contains N space
separated numbers where i − th of the numbers is p_i denoting the total price of the items the
residents of house i are willing to buy if he does not sell to any neighboring house of i. 
Below is a sample input.

10
50 10 12 65 40 95 100 12 20 30

The above input shows that there are 10 houses. The first house will buy items worth of 50
and so on.



Output:
The program must ask the user to enter a value of k. Depending on the value of k, the program must
generate output in two lines. The first line must give the house numbers he must sell to in order
to maximize his sale. The house numbers must be printed in ascending order. The second line
must print the total sale if he sells to these houses. 

Below are some sample outputs for the above input file for different values of k.

Enter value of k: 1
Houses: 1 4 6 8 10
Total Sale: 252

Enter value of k: 2
Houses: 1 4 7 10
Total Sale: 245

Enter value of k: 3
Houses: 1 6 10
Total Sale: 175

Enter value of k: 10
Houses: 7
Total Sale: 100



Algorithm:
The problem can be approached using dynamic programming to ensure the solution 
adheres to the time and space complexity requirements. The algorithm needs to:
1. Parse the input file to retrieve the values of N and the list of prices p.
2. Prompt the user to input the value of k.
3. Use a dynamic programming approach to calculate the maximum possible sales 
while respecting the neighborhood constraint defined by k.
4. Print the optimal set of house numbers and the corresponding total sale amount.



Thought:
In this question, the base case is when there is no house. The optimal structure is when the 
number of houses increases, the maximum sales of the houses if the salesman sell anything to 
certain houses. 

First, I initialize two array, memo and position. The memo array memoise the maximum sales of 
the houses. The position array memoise where the maximum value come from (index of 
previous houses). For each house, I calculate the maximum sales using max(include,exclude), 
include is the maximum sales which include the current houses, value[i] + memo[i-k-1], while 
exclude is the maximum value which exclude the current houses, memo[i-1]. The answer of the 
question is the last value in the memo array (the maximum sales). The worst-case space and 
time complexity is O(N), where N is the total number of houses as I only loop N times, also 
create memo and position array which only take O(N) space.

"""


def maxPrice(value, N, k):
    """
    Initialize the memo array to memoise the max value of houses
    and position to memoise where the max value come from (index of previous houses)
    The optimal base case is when there is no house.
    When index of houses increases, memo[i] = max(include,exclude)
    include : the max value include the current houses, value[i] + memo[i-k-1]
    exclude : the max value exclude the current houses, memo[i-1]
    complexity : space - O(N), N is the total number of houses
                 time - O(N)
    argument : value - the total price of the item for each house 
               N - the total number of houses
               k - number of adjacent of the houses
    return : memo - the max value of the houses for each house
             position - the list of positions
    """
    memo = [None for i in range(N + 1)]
    position = [None for i in range(N + 1)]
    memo[0] = 0  # max value is 0 when there is no house
    memo[1] = value[1]  # max value is first value when there is only 1 house
    position[0] = 0
    position[1] = 0  # position for only 1 house is 0

    for i in range(2, N + 1):
        exclude = memo[i - 1]
        exIndex = i - 1
        if i <= k:
            include = value[i]
            inIndex = 0  # value is based on index 0
        else:
            include = value[i] + memo[i - k - 1]
            inIndex = i - k - 1
        if exclude > include:
            memo[i] = exclude
            position[i] = exIndex
        else:
            memo[i] = include
            position[i] = inIndex
    return memo, position


def backtracking(N, position):
    """
    Backtrack the array position to get index of houses which give the max sale
    If position[i] == (i-1), it means the max sale is come from previous houses,
    hence i-- to the previous houses
    complexity : space : O(N), where N is the total number of houses
                 time : O(N)
    argument : position - the list of positions
                N - total number of houses
    return : index - list of index of the houses which give the max sale
    """
    i = N
    index = []
    while i > 0:
        if i == 1:
            index.append(i)
        if position[i] == (i - 1):
            i -= 1
        else:
            index.append(i)
            i = position[i]
    return index


def printResult(index, memo, N):
    """
    Print the ID of houses and the total sale in given format
    complexity : space:O(N), where N is the length of index
                 time : O(N), where N is the length of index
    argument : index - list of index of the houses which give the max sale
               memo - the max value of the houses for each house
               N - total number of houses
    return : -
    """
    string = "Houses : "
    for i in range(len(index) - 1, -1, -1):
        string += str(index[i]) + " "
    print(string)
    print("Total Sale : " + str(memo[N]))


if __name__ == "__main__":
    filename = "./Sample Data/travellingSalesmanSampleData.txt"
    file = open(filename, "r", encoding="UTF-8-sig")
    tmp = []
    for line in file:
        line = line.strip("\n")
        line = line.split(" ")
        tmp.append(line)
    file.close()

    """
    N is the total number of houses
    value is the total price of the item for each house
    """
    N = int(tmp[0][0])
    value = [0]
    for i in range(N):
        value.append(int(tmp[1][i]))

    k = int(input("Enter value of k : "))
    tmp = maxPrice(value, N, k)
    memo = tmp[0]
    position = tmp[1]
    index = backtracking(N, position)
    printResult(index, memo, N)

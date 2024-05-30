"""
Author: Loi Chai Lam
Date: 15 Mar 2017

Movie Buddy Recommendation using Sorting Algorithm
Assignment 1b

Problem:
Alice has written a script to obtain a file called favoriteMovies.txt 
(stored as "movieBuddyRecommendationSampleData.txt" under "SampleData" folder) 
which contains favorite movies for each user. The favorite movies for each user are not listed in any particular order.
She wants to introduce a movie buddy recommendation feature that sends people notification
about other people who like exactly the same set of movies. She wants to write an
algorithm that generates groups of people who like exactly the same set of movies. 



Requirement:
Let U be the total number of users, C be the maximum number of characters in any movie and
K be the maximum number of movies liked by a user. The total space taken by the input file
favoriteMovies.txt is O(UCK) because the total number of characters is at most U × C × K.
The algorithm must report all groups in O(UCK) time using O(UCK) space. Note that this
time complexity is optimal because reading the input itself takes O(UCK). In other words,
such an algorithm would be optimal. 

You may need to use a linear sorting algorithm (i.e., a sorting algorithm that runs in O(N) where N is the input size).
Recall that, string comparison (e.g., str1<str2 or str1 == str2)
takes O(L) in the worst-case where L is the number of characters in the smaller string



Input:
The input file has for each user, a list of its favorite movies.
Below are the first five lines from the file"

1:FANTASTIC FOUR,THE SECOND BEST EXOTIC MARIGOLD HOTEL
2:THE PEANUTS MOVIE,GET HARD,THE SECOND BEST EXOTIC MARIGOLD HOTEL,PIXELS,THE
WEDDING RINGER,UNFRIENDED,SICARIO
3:UNFRIENDED,THE SECOND BEST EXOTIC MARIGOLD HOTEL,THE WEDDING RINGER,GET
HARD,ALVIN AND THE CHIPMUNKS THE ROAD CHIP
4:MINIONS,UNFRIENDED,CRIMSON PEAK,SICARIO,SPY
5:PAPER TOWNS,THE PERFECT GUY,ENTOURAGE,CREED,INSIDE OUT,A WALK IN THE WOODS,
THE AGE OF ADALINE

Each user ID and its list of movies is separated by a colon :. In each list, movie names are
separated by a comma (,). You can safely assume that the movie names consist only of letters
from English alphabet in upper case. 



Output:
The program must print groups of users (of size at least 2)
such that all users in a group like exactly the same set of movies. 

Below is a sample output for the above file.

GROUP 1
Movies: JURASSIC WORLD,A WALK IN THE WOODS
Buddies: 5921,8894

GROUP 2
Movies: THE SECOND BEST EXOTIC MARIGOLD HOTEL,THE VISIT,NO ESCAPE,SISTERS,
MINIONS,PADDINGTON,BLACK MASS
Buddies: 2819,6836,8294,8573

GROUP 3
Movies: WAR ROOM,TRAINWRECK,CHAPPIE,STRAIGHT OUTTA COMPTON
Buddies: 1672,2007,6710

GROUP 4
Movies: THE AGE OF ADALINE,FANTASTIC FOUR,SICARIO,TOMORROWLAND
Buddies: 299,3871,6738,9758,9993

GROUP 5
Movies: INSIDE OUT,HOT PURSUIT,UNFRIENDED,KRAMPUS
Buddies: 6582,9711

GROUP 6
Movies: WAR ROOM,MINIONS,JURASSIC WORLD,INSIDE OUT
Buddies: 1205,5890

GROUP 7
Movies: SICARIO,MAGIC MIKE XXL,SISTERS,TOMORROWLAND,SPY
Buddies: 3921,4607,5161,6931,7433,7452

GROUP 8
Movies: THE PEANUTS MOVIE,MINIONS,STRAIGHT OUTTA COMPTON,THE INTERN
Buddies: 3250,8428

In the above output, the users in each group like exactly the same movies. 
In your output, the order of groups does not matter as long as you list all groups with their
movies and users. Similarly, the order of movies and users in a group also does not matter.



Thought:
Note: U –total number of users, C - maximum number of characters in any movie, K - maximum 
number of movies liked by a user

First, the file is read and each user is put with one of their movies into a list of list, the 
length of the list of list is UK. The worst-case time complexity is O(UK), the worst-case space 
complexity is O(UCK). 

To assign the name of the movies into a unique identifier, I rearrange the name of movies using 
radix sort. The worst-case time complexity and space complexity for radix sort the characters are 
both O(UCK). Next, I compare the name of the movies one by one. If the names are same, the id 
is assigned. If the names are not same, the counter is added by one, the movie is appended to the 
list movieName and the comparison string changed. It takes O(UK) worst-case time complexity 
and O(UCK) worst-case space complexity. After that, I group the movies into a list of list which 
contain tuple of first element: the user id, and second element: the list of ids of movies liked by 
that user. Both the worst-case space and time complexity are O(UK). Finally, I sort the list of ids
of movies using radix sort and print out the result to screen. The worst-case time and space 
complexity are O(UK) for sorting and printing the result.

Hence, the total worst-case time complexity and total worst-case space complexity are O(UCK)

"""


def readFile(filename):
    """
    To read the file and separate it into list of list
    time complexity: worst : O(UK)
    space complexity : worst : O(UCK)
    argument : filename : the filename which need to be read 
    return : array - the array ,user - number of users

    """
    array = []
    file = open(filename, "r", encoding="UTF-8-sig")
    user = 0
    for line in file:
        line = line.strip("\n")
        line = line.replace(":", ",")
        line = line.split(",")
        user += 1
        for i in range(1, len(line)):
            array.append([int(line[0]), line[i]])
    file.close()
    return array, user


def getColumn(array, position):
    """
    Find column of the list of list depend on position
    time complexity :worst : O(UK),for character ; O(U),for numbers
    space complexity : worst :O(UCK+UK),for character ; O(UK+U),for numbers
    argument :array - the list of list
               position - the index of the list of list
    return : tmp - the column array of the list of list
    """
    tmp = []
    for i in range(len(array)):
        if (position + len(array[i][1])) >= 0:
            tmp.append(array[i][1][position])
    return tmp


def findMaxInList(array, thetype):
    """
    Find the maximum number of the list
    time complexity :worst : O(U),for number ; O(UK) for character
    space complexity : worst :O(U),for number ; O(UK) for character
    argument :array - the list
            thetype - "number" : find the maximum number
                    - "character" : find the maximum ord of the characters
    return : maximum - the maximum num / ord of the list 
    """
    if thetype == "number":
        maximum = array[0]
        for i in range(len(array)):
            if array[i] > maximum:
                maximum = array[i]
    elif thetype == "character":
        maximum = ord(array[0])
        for i in range(len(array)):
            if ord(array[i]) > maximum:
                maximum = ord(array[i])
    return maximum


def findMaxLength(array):
    """
    Find the maximum length of the list in list of list
    time complexity :worst : O(UK),for character ; O(U),for numbers
    space complexity : worst :O(UCK),for character ; O(UK),for numbers
    argument :array - the list of list
    return : maximum - the maximum length of list in the list of list
    """
    maximum = len(array[0][1])
    for i in range(1, len(array)):
        if len(array[i][1]) > maximum:
            maximum = len(array[i][1])
    return maximum


def countingSort(array, position, thetype):
    """
    Use Counting sort to sort the list of characters or numbers
    time complexity :worst : O(U)orU(K),for number ; O(UK),for characters
    space complexity : worst : O(UK),for number ; O(UCK),for characters
    argument :array - the list of list which contain userId and list of movie's id/movie's name
              thetype : number - sort the numbers in list of list
                        character - sort the characters in list of list
                        position - the position of the character/number to be sorted
    return : output - the sorted list
    """
    output = []
    count = []
    tmp = getColumn(array, position)
    maximum = findMaxInList(tmp, thetype)
    for i in range(maximum + 1):
        count.append([])
    if thetype == "number":
        for i in range(len(array)):
            if (position + len(array[i][1])) >= 0:
                index = array[i][1][position]
                count[index].append(array[i])
            else:
                count[0].append(array[i])
    elif thetype == "character":
        for i in range(len(array)):
            if (position + len(array[i][1])) >= 0:
                index = ord(array[i][1][position])
                count[index].append(array[i])
            else:
                count[0].append(array[i])
    for i in range(len(count)):
        numOccur = len(count[i])
        for j in range(numOccur):
            output.append(count[i][j])
    return output


def radixSort(array, thetype):
    """
    Use Radix sort to sort the list of list of characters or numbers
    time complexity :worst : O(UK),for number ; O(UCK),for characters
    space complexity : worst : O(UK),for number ; O(UCK),for characters
    argument :array - the list of list which contain userId and list of movie's id/movie's name
              thetype : number - sort the numbers in list of list
                        character - sort the characters in list of list
    return : output - the sorted list of list 
    """
    maxLength = findMaxLength(array)
    position = -1
    output = array[:]
    while position >= -maxLength:
        output = countingSort(output, position, thetype)
        position -= 1
    return output


def movieToNum(array):
    """
    Assign a unique index to moviename 
    time complexity :worst : O(UK)
    space complexity : worst :O(UCK+K)
    argument :array - the sorted list of list which contain userId and its movie names
    return : movieName - the list of movies
    """
    movieName = []
    compareString = array[0][1]
    movieName.append(array[0][1])
    j = 0
    array[0][1] = j
    for i in range(1, len(array)):
        if array[i][1] == compareString:
            array[i][1] = j
        else:
            movieName.append(array[i][1])
            j += 1
            compareString = array[i][1]
            array[i][1] = j
    return movieName


def groupMovie(array, user):
    """
    Group the movie to same user ID
    time complexity :worst : O(U+UK)
    space complexity : worst :O(UK+UK)
    argument :array - the list of list which contain userId and its movie's id
              user - number of users
    return : grp - the list of list contains list of movie number 
    """
    grp = []
    for i in range(user):
        grp.append([])
    for i in range(len(array)):
        grp[array[i][0] - 1].append(array[i][1])
    return grp


def addUserId(array):
    """
    Add the user id to the grouped movies
    time complexity :worst : O(U)
    space complexity : worst :O(UK)
    argument :array - the list of list contains list of movie number
    return : array - the list of tuple which contains first: user ID
                    and second: the list of sorted movies
    """
    for i in range(len(array)):
        array[i] = (i + 1, array[i])
    return array


def printResult(array, movieName):
    """
    Print the group of same users which like same movies
    time complexity :worst : O(UK)
    space complexity : worst :O(UK)
    argument :array - the sorted list of list which contain userId and list of movie's id
              movieName : the array of movies names
    return : -
    """
    compareArray = array[0][1]
    flag = True
    count = 1
    userStr = "Buddies : "
    for i in range(1, len(array)):
        if array[i][1] == compareArray:
            userStr += str(array[i - 1][0]) + " , "
            if flag == True:
                print("GROUP " + str(count))
                count += 1
                movieStr = "Movies : "
                for j in range((len(array[i - 1][1])) - 1):
                    movieStr += movieName[array[i - 1][1][j]] + " , "
                movieStr += movieName[array[i - 1][1][j + 1]]
                flag = False
                print(movieStr)
        else:
            userStr += str(array[i - 1][0])
            if flag == False:
                print(userStr)
                print()
            userStr = "Buddies : "
            flag = True
            compareArray = array[i][1]
    if flag == False:
        print(userStr)
        print()


if __name__ == "__main__":
    filename = "./SampleData/movieBuddyRecommendationSampleData.txt"
    array, user = readFile(filename)
    array = radixSort(array, "character")
    movieName = movieToNum(array)
    array = groupMovie(array, user)
    array = addUserId(array)
    array = radixSort(array, "number")
    printResult(array, movieName)

"""
Total Time complexity : O(UCK)
Total Space complexity : O(UCK)
"""

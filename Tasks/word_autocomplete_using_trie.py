"""
Author: Loi Chai Lam
Date: 29 May 2024

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
Once you have created a Trie, the program must ask the user to enter a prefix. It must then
display the word with the highest frequency, its definition and the number of words that have
the input text as the prefix. If there are more than one words with the highest frequency, you
must display the alphabetically smallest word (e.g., if prefix is “be”, and “best” and “beast”
both have the same frequency (and highest among all words matching the prefix), your program
must display “beast” because it is alphabetically smaller than “best”). The program must keep
asking the user to enter another prefix and terminate only when the user enters *** instead of
the prefix. Below is a sample execution of the program for the small data shown in the Input
section above.
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



Algorithm:
To solve this problem, a dynamic programming approach similar to the knapsack problem can be used. 
The algorithm needs to:
1. Parse the input file to retrieve N and the list of song durations d.
2. Prompt the user to enter the journey time T.
3. Use a dynamic programming table to keep track of possible durations that can be achieved with subsets of songs.
4. Construct the playlist from the dynamic programming table if a valid combination is found.
5. Print the playlist in ascending order of song IDs or report "Bad luck Alice!" if no valid playlist is found.



Thought:
In this question, I use the concept of subset sum problem. I create a matrix, dp[N+1][T+1] with 
worst-case space complexity O(NT) to memorize the previous answer, where N is the total 
number of songs and T is the journey time. The optimal base case for this question is when 
there is no song, which is N = 0, an empty subset. I divide it into two sub-problems. 

1. include the subset with last element, then N = N-1, T = T-[value of last element]
2. exclude the subset with last element, then N = N-1, T = T

The final answer of the sum T is in dp[N][T]. When backtracking, I first check whether the 
dp[N][T] is True. If it is False, then there is no solution. If it is True, I keep track of the previous 
subsets until the previous subset is False, then I append the current True subset to a song array. 

The worst-case time complexity for subset sum is O(NT) which I use 2 for loops to loop through 
the matrix, while the worst-case time complexity for backtracking is O(T). The worst-case space 
complexity of backtracking is O(NT).

Hence, the total worst-case time and space complexity for question 2 is O(NT)

"""

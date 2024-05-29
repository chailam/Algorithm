"""
Author: Loi Chai Lam
Date: 29 May 2024

Word AutoComplete using Trie Data Structure
Assignment 3

Problem:
Alice drives to work and listens to her favorite songs on her way. She hates it when she is in
middle of a song and reaches her destination. This is because if she does not listen to a song
till the end then it keeps playing in her mind for the whole day which affects her performance.
She does not want to sit in the car waiting for the song to finish. Also, she does not want to
stop listening to the song before she has arrived her destination. In other words, she wants the
songs to play such that a song ends exactly when she has arrived her destination.

Your goal is to write an algorithm that determines a playlist of the songs such that, if the
songs are continuously played during her journey, a song finishes exactly when she reaches the
destination. In other words, if the estimated duration of her journey is T minutes, the total
duration of the songs in the playlist must also be exactly T. Furthermore, she does not want
any song to be repeated. Therefore, your playlist should not have duplicate songs


Songs Logic:
There are a list of songs numbered 1 to N (called ID of the song). A song with ID i has
a duration d_i (in minutes). You can assume that no two songs have the same duration. The
output must print the playlist meeting the above requirement (in ascending order of the IDs of
the songs). If it is not possible to find such playlist, you must report a message stating “Bad
luck Alice!”.



Requirement:
- The solution must run in worst-case O(NT) time and use O(NT) space,
where N is the total number of songs and T is the estimated journey time



Input:
The input file consists of 2 lines. The first line of the input contains a single integer N that
represents the total number of songs in the phone. The next line contains N space separated
numbers where i − th of the numbers is d_i denoting the duration of the song with ID i. Below
is a sample input

5
10 3 5 7 2

In the above input, there are 5 songs: duration of song with ID 1 is 10 minutes, and the
song with ID 2 is 3 minutes and so on.



Output:
The program must ask the user to enter the journey time T (which you can assume will always
be a positive integer). Your output must print the playlist that meets the above requirements,
in ascending order of IDs, with the duration of each song displayed next to the song ID (see
below). If there are more than one correct answers (multiple playlists with the total duration
T), you are free to print any of the playlists. If it is not possible to find such a playlist, you
must display “Bad luck Alice!”

Below are some sample outputs for different values of trip length T.

Enter trip length: 14
Playlist
ID: 3 Duration: 5
ID: 4 Duration: 7
ID: 5 Duration: 2

Enter trip length: 17
Playlist
ID: 1 Duration: 10
ID: 4 Duration: 7

Note that the following answer for T = 17 is also correct.
Enter trip length: 17
Playlist
ID: 1 Duration: 10
ID: 3 Duration: 5
ID: 5 Duration: 2

If the trip length is 16, no playlist can be found that has the total duration equal to 16 .
Enter trip length: 16
Bad Luck Alice!



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

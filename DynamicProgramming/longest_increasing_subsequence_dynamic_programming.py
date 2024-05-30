"""
Author: Loi Chai Lam
Date: 7 Mar 2024

Longest Increasing Subsequence for Dynamic Programming

Week 4 FIT 2004 Lab

Problem:
Given a sequence of numbers, the longest increasing subsequence problem is 
to find the longest subsequence in the list which is sorted in ascending order. 

Assume that the values are all POSITIVE values

Example:
For example, if a list is {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13,
3, 11, 7, 15} then the longest increasing subsequence is {0, 2, 6, 9, 11, 15}
because there is no subsequence in this list that is in ascending order
and is longer than this.
The answer for the above example is 6

Thought:
We can initialize an array dp of the same length as the input array nums, 
where dp[i] represents the length of the longest increasing subsequence ending at index i. 
We can iterate through the array and update dp based on the elements before the current index. 
The final result will be the maximum value in the dp array.
"""


def lengthOfLIS(alist):
    n = len(alist)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if alist[i] > alist[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)





if __name__ == "__main__":
    alist = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13,
             3, 11, 7, 15]

    print(lengthOfLIS(alist))

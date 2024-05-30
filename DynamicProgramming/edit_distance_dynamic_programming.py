"""
Author: Loi Chai Lam
Date: 7 Mar 2024

Edit Distance for Dynamic Programming

Week 4 FIT 2004

Problem:
Edit distance is the minimum number of edit operations required to convert one sequence into another


Example: 
Edit distance between computer and commuter is 1
Edit distance between sport and sort is 1.

Thought:
We want to convert s1 to s2 containing n and m letters, respectively. 
Assume we have computed and memoized the optimal solution for all sub-problems (e.g., convert s1[1…n-1] to s1[1…m-1])

Scenario 1:
If s1[n] == s2[m]
		cost = dist(s1[1…n-1],s2[1… m-1])


Scenario 2:
if optimal solution is substituting s1[n] with s2[m]
		cost = 1 + dist(s1[1…n-1],s2[1…m-1])


Scenario 3:
if optimal solution is adding s2[m] in s1 after s1[n]
		cost = 1 + dist(s1[1…n],s2[1…m-1])


Scenario 4:
if optimal solution is removing s1[n]
 		cost = 1 + dist(s1[1…n-1],s2[1…m])

From above , the minimum cost is 
cost = 1 + 
Min (dist(s1[1…n-1],s2[1…m-1]),
       dist(s1[1…n],s2[1…m-1])
       dist(s1[1…n-1],s2[1…m])
        )

Use a temporary array, dp, to hold the previous edit distance.

"""



def editDistanceDP(str1, str2):
    """ 
    We want to convert str1 into str2
    Time complexity: O(nm)
    Space complexity: O(nm)
    where n is length of str1 and m is length of str2

    """
    str1 = str1.lower()
    str2 = str2.lower()
    lStr1 = len(str1)
    lStr2 = len(str2)

    # contruct a x*m matrix where n is length of str1 and m is length of str2
    dp = [[0] * (lStr2 + 1) for i in range(lStr1 + 1)]

    # initialize the value
    for i in range(lStr1 + 1):
        dp[i][0] = i

    for j in range(lStr2 + 1):
        dp[0][j] = j

    for i in range(1, lStr1 + 1):
        for j in range(1, lStr2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                print(i, j)
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

    return (dp[lStr1][lStr2], dp)


def backtrack(str1, str2, dp):
    """
    Recall: Diagonal means substitution if letters are not same
            Upward arrow means removing the letter str1[i]
            Left arrow means adding the letter str2[i] in str

    """
    lStr1 = len(str1)
    lStr2 = len(str2)

    # starting from the dp[lStr1]lStr2]
    i = lStr1
    j = lStr2

    while i > 0 and j > 0:
        up = dp[i - 1][j]
        left = dp[i][j - 1]
        diagonal = dp[i - 1][j - 1]
        if str1[i - 1] == str2[j - 1]:
            print("same character", str1[i - 1], "no change, move on to next")
            i = i - 1
            j = j - 1
            print(str1, str2)
        # compare amount three direction to find the smallest
        elif (up <= left) & (up <= diagonal):
            # if up is the smallest, remove letter str1[i]
            print("remove letter", str1[i - 1])
            str1 = str1[:i - 1] + str1[i:]
            print(str1, str2)
            i = i - 1
        elif (left <= up) & (left <= diagonal):
            # if left is the smallest
            print("adding letter", str2[j - 1])
            str1 = str1[:i] + str2[j - 1] + str1[i:]
            print(str1, str2)
            j = j - 1
        elif (diagonal <= up) & (diagonal <= left):
            # if diagonal is the smallest
            print("substitute letter", str1[i - 1], "with", str2[j - 1])
            str1 = str1[:i - 1] + str2[j - 1] + str1[i:]
            print(str1, str2)
            i = i - 1
            j = j - 1
    return str1








if __name__ == "__main__":
    str1 = "sport"
    str2 = "sort"
    (minEdit, dp) = editDistanceDP(str1, str2)
    print("minimum edit is", minEdit)
    print(dp)
    backtrack(str1, str2, dp)

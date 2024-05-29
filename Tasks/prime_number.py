"""
Name : Loi Chai Lam
Date : 5/3/2018

Write a program to print all prime numbers between 1 and N.
Explore more efficient ways to print prime numbers between 1 and N.


"""

def prime(N):
    """
    O(n^2)
    """
    for i in range(2,N+1):
        flag = False
        for j in range(2,i):
            if i % j == 0:
                flag = True
        if flag == False:
            print(i)

def prime_medium(N):
    """
    Only look up till the square root, so is O(log(n)).
    As prime of 8: 1*8, 2*4, 4*2, 8*1, is a mirror of (8)^0.5
    """
    break
    
def prime_good(N):
    """
    start from 2, 2 is a prime, remove every multiplication of 2
    3 is prime, remove every multiplication of 3
    4 is already the multiply of 2, has been removed
    5 is prime, remove every multiplication of 5.
    Complexity is O(n(log(n)))
    """
    break

prime(11)
        

"""
author : Loi Chai Lam
date : 23 Aug 2017

Shaker Sort

Also known as bidirectional bubble sort,cocktail sort, shaker sort, 
ripple sort, shuffle sort, or shuttle sort, is an extension of bubble sort. 
The algorithm extends bubble sort by operating in two directions. 
While it improves on bubble sort by more quickly moving items to the beginning of the list, 
it provides only marginal performance improvements.

It is used primarily as an educational tool.


"""



def shaker_sort(a_list):
    """
    Use the shaker sort to sort the list
    argument = a_list - the list
    return  = -    
    """
    n = len(a_list)
    start_left = 0
    start_right = n - 1
    end_left = n - 1
    end_right = 0
    for j in range(n - 1):
        breakFlag = True
        if j % 2 == 0:
            for i in range(start_left, end_left, 1):
                if a_list[i] > a_list[i + 1]:
                    a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                    breakFlag = False
            end_left -= 1  # every time swapping, one larger element will move to right
            start_right -= 1
            if breakFlag == True:
                break
        else:
            for i in range(start_right, end_right, -1):
                if a_list[i] < a_list[i - 1]:
                    a_list[i], a_list[i - 1] = a_list[i - 1], a_list[i]
                    breakFlag = False
            start_left += 1
            end_right += 1
            if breakFlag == True:
                break
    return a_list

#Selection Sort

def getMinIndex(myList, start, stop):
   min_index = start
   for i in range(start,stop):
      if myList[i] < myList[min_index]:
         min_index = i
   return min_index

aList = [2,6,87,4,7,5,2,6]
n = len(aList)   
for index in range(n):
    min_pos = getMinIndex(aList, index, n)    #Find the index position of min number
    b = aList[index]     #Save the number in the list that would be changed to a
    aList[index] = aList[min_pos]     #Put the min number to the eg. 0th index in the first round of loop
    aList[min_pos] = b     #Put the saved number to the index position which the min number had stayed(SWAP)

print(aList)    

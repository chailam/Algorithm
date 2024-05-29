#Selection Sort2 (based on lecture slides)

def getMinIndex(myList, start, stop):
   min_index = start
   for i in range(start,stop):
      if myList[i] < myList[min_index]:
         min_index = i
   return min_index

def swapElements(myList,i,j):
   temp = myList[i]
   myList[i] = myList[j]
   myList[j] = temp
   
aList = [7,2,11,8,4,2,5,6]
n = len(aList)   
for index in range(n):
   #Find position of the smallest number in aList[index:]
   min_position = getMinIndex(aList,index,n)
    
  #Swap numbers at “index” and “min_position”
   swapElements(aList,index,min_position)

print(aList)

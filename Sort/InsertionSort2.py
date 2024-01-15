# Insertion Sort2 (based on lecture slides)

#swap elements in a list at indices i and j
def swapElements(myList,i,j):
   temp = myList[i]
   myList[i] = myList[j]
   myList[j] = temp

aList = [6,5,3,1,8,7, 2, 4]
n = len(aList)   
for index in range(1,n):
   #insert aList[index] in aList[0:index] in sorted order
   position = index
   while aList[position-1] > aList[position] and position>0:
      #swap elements at aList[position] and aList[position+1]
      swapElements(aList,position-1,position)
      position = position-1
   
print(aList)

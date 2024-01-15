#InsertionSort
alist = [4,1,3,2,18,30,12,5]
n = len(alist)

for index in range(1,n):
    currentvalue = alist[index] #Save the value first
    position = index #Save the position

    while position>0 and alist[position-1]>currentvalue: #position>0 to compare the rest of the front value
        alist[position]=alist[position-1] #If true put the value into it
        position = position-1  #this is hv to compare when the list going longer
        
    alist[position]=currentvalue    #Get back the value
       
print(alist)

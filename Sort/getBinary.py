def getBinaryRep(N):
    bitList = []
    while N != 0:
	    # determine the least significant bit and add to bitList
        if N%2 == 1:
            bitList = [1] + bitList
        else:
            bitList = [0] + bitList
	    # remove the least significant bit
        N = N//2
    return bitList

NumOfItems = 4
AllSubsets = []
for i in range(2**NumOfItems):
	# using the function from previous slide
    subset = getBinaryRep(i)
	# add zeroes to get length equal to NumOfItems
    while len(subset) < NumOfItems:
        subset = [0] + subset
    AllSubsets.append(subset)

print(AllSubsets)
    

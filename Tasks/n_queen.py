"""
Name : Loi Chai Lam
Date : 14 Jun 2017

N Queen Problem

N - Queens problem is to place n - queens in such a manner on an n x n chessboard 
that no queens attack each other by being in the same row, column or diagonal.


"""
# check if a queen A attacks another queen B.
# They are in the same diagonal if absolute difference in their row numbers = absolute difference intheir column numbers


def attack(A_row, A_col, B_row, B_col):
    if A_row == B_row:
        return True
    if abs(A_col - B_col) == abs(A_row - B_row):
        return True
    return False

# check if the queen at (my_row,my_col) is attacked by queens in partial solution


def isAttacked(my_row, my_col, partialSolution):
    for qCol in range(len(partialSolution)):
        qRow = partialSolution[qCol]
        if attack(qRow, qCol, my_row, my_col):
            return True
    return False

# get the next possible solution


def getPositions(partialSolution, n):
    position = []
    my_col = len(partialSolution)
    for my_row in range(n):
        if not isAttacked(my_row, my_col, partialSolution):
            position.append(my_row)
    return position


def printTable(n, partialSolution, position):
    table = []
    for i in range(n):
        table.append([])
        for j in range(n):
            table[i].append(0)
    for col in range(len(partialSolution)):
        row = partialSolution[col]
        table[row][col] = "Q"
    pos_col = len(partialSolution)
    for i in range(len(position)):
        pos_row = position[i]
        table[pos_row][pos_col] = "X"
    print(table)


def nQueen(partialSolution, n, completeSolution):
    position = getPositions(partialSolution, n)
    if len(position) == 0:
        if len(partialSolution) == n:
            # printTable(n,partialSolution,[])
            print(partialSolution)
            completeSolution.append(1)
    else:
        for item in position:
            partialSolution.append(item)
            nQueen(partialSolution, n, completeSolution)
            partialSolution.pop()


n = int(input("Enter value for n : "))
partialSolution = []
completeSolution = []
nQueen(partialSolution, n, completeSolution)
print("There are", len(completeSolution), "solutions.")

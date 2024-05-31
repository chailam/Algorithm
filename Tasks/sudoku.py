"""
Author: Loi Chai Lam
Date: 23 Apr 2017

Title: Sudoku SolvingThis problem is using recursive way to find
the value in sudoku.

"""


import copy


def checkDuplicate(aList, num):
    for i in aList:
        if i == num:
            return True
    return False


def valid_entry(grid, num, r, c):
    valid = False
    rowVal = grid[r]
    colVal = []
    subgridVal = subgrid_values(grid, r, c)
    for i in range(len(grid)):
        colVal.append(grid[i][c])

    if (checkDuplicate(rowVal, num) == False) and (checkDuplicate(colVal, num) == False) and (checkDuplicate(subgridVal, num) == False):
        valid = True
    return valid



def subgrid_values(grid, row, col):
    val = []
    # get dimension of inner box
    n = int(len(grid)**(0.5))
    r = (row // n) * n
    c = (col // n) * n
    for i in range(r, r + n):
        for j in range(c, c + n):
            val.append(grid[i][j])
    return val


def grids_augmented_in_row(grid, num, r):
    col = len(grid)
    augGrid = []
    for c in range(col):
        if (valid_entry(grid, num, r, c) == True):
            if grid[r][c] == "x":
                newGrid = copy.deepcopy(grid)
                newGrid[r][c] = num
                # print(newGrid)
                augGrid.append(newGrid)
        elif grid[r][c] == num:
            augGrid.append(grid)
            return augGrid

    return augGrid



def grids_augmented_with_number(grid, num):
    n = len(grid)
    i = n - 1  # last row
    result = []
    return recursiveAug(result, grid, num, i)




def recursiveAug(result, grid, num, n):
    if n < 0:
        result.append(grid)
        # print(result)
        return result
    else:
        augList = grids_augmented_in_row(grid, num, n)
        for l in augList:
            recursiveAug(result, l, num, n - 1)
        return result


def solve_sudoku(grid):
    n = len(grid)
    sudResult = []
    print(recursiveSudoko(sudResult, grid, n))



def recursiveSudoko(sudResult, grid, num):
    if num < 1:
        sudResult.append(grid)
        # print(sudResult)
        return sudResult
    else:
        sudList = grids_augmented_with_number(grid, num)
        for l in sudList:
            recursiveSudoko(sudResult, l, num - 1)
        return sudResult


def test(grid):
    aa = grids_augmented_with_number(grid, 1)
    for i in aa:
        bb = grids_augmented_with_number(i, 2)
        for j in bb:
            cc = grids_augmented_with_number(j, 3)
            for k in cc:
                dd = grids_augmented_with_number(k, 4)
                print(dd)






grid = [[1, "x", "x", "x"], ["x", "x", "x", "x"], ["x", "x", "x", "x"], ["x", 2, "x", "x"]]
grid1 = [[2, "x", "x", "x"], ["x", 3, 2, 4], ["x", "x", 4, 2], [1, 2, 3, "x"]]
gridA = [["x", "x", 1, "x"], [4, "x", "x", "x"], ["x", "x", "x", 2], ["x", 3, "x", "x"]]

gridB = [[1, "x", 9, "x", "x", "x", "x", 6, "x"],
         [8, 4, "x", "x", 1, "x", "x", 7, 5],
         ["x", "x", 2, "x", "x", 3, "x", "x", 4],
         ["x", "x", 8, 3, 2, 1, "x", 4, 7],
         ["x", "x", 5, "x", "x", "x", 6, "x", "x"],
         [4, 2, "x", 6, 9, 5, 8, "x", "x"],
         [7, "x", "x", 1, "x", "x", 4, "x", "x"],
         [6, 9, "x", "x", 8, "x", "x", 5, 3],
         ["x", 5, "x", "x", "x", "x", 7, "x", 9]]




# print(grids_augmented_in_row(grid,1,0))
# grids_augmented_with_number(grid,1)
solve_sudoku(gridB)

"""
author : Loi Chai Lam
date   : 7 Sep 2017

Simple Board Game

Description:
The Knight in Chess moves in a way that can be considered to be a
combination of two simpler moves, namely either move two squares
either horizontally followed by one square vertically, or move two
squares vertically followed by one square horizontally


The objective of this program is to find a sequence of moves that allows a Knight in chess
 visit every square on the chessboard exactly once and return to the starting square.
 The program includes a Python class Tour to represent the chessboard, track the knight's moves,
 and determine possible next moves.


"""


class Tour():
    gameID = 0

    def __init__(self, size=8):  # default value
        self._board = [['0'for i in range(size)]for j in range(size)]
        self._board[0][0] = "K"
        Tour.gameID += 1
        self.id = Tour.gameID

    def __str__(self):
        output = "Game:" + str(self.gameID)
        output += "\n" + "=================================================="
        for row in self._board:
            output += "\n" + str(row)
        return output

    def _find(self, target):  # private function
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                if self._board[i][j] == target:
                    return i, j
        return -1, -1

    def position(self, x, y):
        assert self.valid(x, y), "invalid row col"
        i, j = self._find("K")
        if i != -1 and j != -1:
            self._board[i][j] = "*"
        self._board[x][y] = "K"

    def valid(self, x, y):
        if 0 <= x <= len(self._board):
            if 0 <= y <= len(self._board):
                return True
        return False


    def nextmoves(self):  # [row][column]
        move = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]
        possible = []
        i, j = self._find("K")
        if not self.valid(i, j):
            return []
        for trymove in move:
            x = i + trymove[0]
            y = j + trymove[1]
            if self.valid(x, y) and self._board[x][y] != "*":
                possible.append([x, y])
        return possible


if __name__ == "__main__":
    game = Tour()
    while True:
        print(game)
        option = int(input("if continue : 1, quit : 2 \n"))
        assert option == 1 or option == 2, "invalid option"
        if option == 2:
            break
        possible = game.nextmoves()
        print("Possible : " + str(possible))
        userChoose = int(input("Choose the possible next[first=0 ] : "))
        assert 0 <= userChoose <= len(possible), "invalid possible"
        game.position(possible[userChoose][0], possible[userChoose][1])

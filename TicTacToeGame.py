import copy


class TicTacToeBoard:
    def __init__(self):
        self.board = [[None, None, None], [None, None, None], [None, None, None]]

    def isGameOver(self):
        return self.isGameWon() or self.isCatsGame()

    def isCatsGame(self):
        if (not self.isGameWon()):
            for row in self.board:
                for item in row:
                    if not item:
                        return False
            return True
        return False

    def isGameWon(self):
        isWon = self.isCrossWon()
        if (not isWon):
            for i in range(3):
                isWon = self.isRowWon(i) or self.isColumnWon(i)
                if isWon:
                    break
        if isWon:
            return isWon
        else:
            return False

    def isRowWon(self, row):
        return self.board[row][0] is not None and self.board[row][0] == self.board[row][1] == self.board[row][2]

    def isColumnWon(self, column):
        return self.board[0][column] is not None and self.board[0][column] == self.board[1][column] == self.board[2][
            column]

    def isCrossWon(self):
        return self.board[0][0] is not None and self.board[0][0] == self.board[1][1] == self.board[2][2] or None != \
               self.board[0][2] and self.board[0][2] == self.board[1][1] == self.board[2][0]

    def putX(self, x, y):
        if not self.isPointTaken(x, y):
            self.board[x][y] = "X"
        else:
            print("cannot put X in {},{}".format(x, y))

    def putO(self, x, y):
        if not self.isPointTaken(x, y):
            self.board[x][y] = "O"
        else:
            print("cannot put O in {},{}".format(x, y))

    def isPointTaken(self, x, y):
        return self.board[x][y] is not None

    def printBoard(self, pointer_location):
        display_board = copy.deepcopy(self.board)
        current_value_at_pointer = display_board[pointer_location[0]][pointer_location[1]]
        if current_value_at_pointer is not None:
            display_board[pointer_location[0]][pointer_location[1]] = "*" + str(current_value_at_pointer) + "*"
        else:
            display_board[pointer_location[0]][pointer_location[1]] = "**"

        i = 0
        for row in display_board:
            print("{}|{}|{}".format(self.getPrintValue(row[0]), self.getPrintValue(row[1]), self.getPrintValue(row[2])))
            if i == 0 or i == 1:
                print("------------")
            i += 1

    def getPrintValue(self, value):
        if value is not None:
            return " {} ".format(value)
        else:
            return "   "

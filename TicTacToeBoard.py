import copy

class TicTacToeBoard:
    def __init__(self):
        self.board=[[None, None, None],[None, None, None],[None, None, None]]

    def is_game_over(self):
        return self.is_game_won() or self.is_cats_game()

    def is_cats_game(self):
        if (not self.is_game_won()):
            for row in self.board:
                for item in row:
                    if not item:
                        return False
            return True
        return False

    def is_game_won(self):
        is_won = self.is_cross_won()
        if not is_won:
            for i in range(3):
                is_won = self.is_row_won(i) or self.is_column_won(i)
                if is_won:
                    break
        if is_won:
            return is_won
        else:
            return False

    def is_row_won(self, row):
        return self.board[row][0] is not None and self.board[row][0] == self.board[row][1] == self.board[row][2]

    def is_column_won(self, column):
        return self.board[0][column] is not None and self.board[0][column] == self.board[1][column] == self.board[2][
            column]

    def is_cross_won(self):
        return self.board[0][0] is not None and self.board[0][0] == self.board[1][1] == self.board[2][2] or \
               self.board[0][2] is not None and self.board[0][2] == self.board[1][1] == self.board[2][0]

    def put_x(self, x, y):
        if not self.is_already_marked(x, y):
            self.board[x][y] = "X"
        else:
            print("cannot put X in {},{}".format(x, y))

    def put_o(self, x, y):
        if not self.is_already_marked(x, y):
            self.board[x][y] = "O"
        else:
            print("cannot put O in {},{}".format(x,y))

    def is_already_marked(self, x, y):
        return self.board[x][y] is not None

    def print_board(self, pointer_location):
        display_board = copy.deepcopy(self.board)
        current_value_at_pointer = display_board[pointer_location[0]][pointer_location[1]]
        if current_value_at_pointer is not None:
            display_board[pointer_location[0]][pointer_location[1]] = "*" + str(current_value_at_pointer) + "*"
        else:
            display_board[pointer_location[0]][pointer_location[1]] = "**"

        i = 0
        for row in display_board:
            print("{}|{}|{}".format(self.get_print_value(row[0]), self.get_print_value(row[1]),
                                    self.get_print_value(row[2])))
            if i == 0 or i == 1:
                print("------------")
            i += 1

    def get_print_value(self, value):
        if value is not None:
            return " {} ".format(value)
        else:
            return "   "





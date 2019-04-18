import shlex

from TicTacToeBoard import TicTacToeBoard


def move_cursor_up(pointer):
    if pointer[0] != 0:
        pointer = (pointer[0] - 1, pointer[1])
    return pointer


def move_cursor_down(pointer):
    if pointer[0] != 2:
        pointer = (pointer[0] + 1, pointer[1])
    return pointer


def move_cursor_left(pointer):
    if pointer[1] != 0:
        pointer = (pointer[0], pointer[1] - 1)
    return pointer


def move_cursor_right(pointer):
    if pointer[1] != 2:
        pointer = (pointer[0], pointer[1] + 1)
    return pointer


print("Player 1 begins.")
print("Type left, right, up, and down to move the pointer.")
print("Type mark to mark the position.")

MARK_O = "O"
MARK_X = "X"
is_player_one = True

new_board = TicTacToeBoard()
cursor_point = (0, 0)
new_board.print_board(cursor_point)

while True:
    cmd, *args = shlex.split(input('> '))

    if cmd == 'left':
        cursor_point = move_cursor_left(cursor_point)
    elif cmd == 'right':
        cursor_point = move_cursor_right(cursor_point)
    elif cmd == 'up':
        cursor_point = move_cursor_up(cursor_point)
    elif cmd == 'down':
        cursor_point = move_cursor_down(cursor_point)
    elif cmd == 'mark':
        if new_board.is_already_marked(cursor_point[0], cursor_point[1]):
            print("This point is already marked!")
        else:
            if is_player_one:
                new_board.put_o(cursor_point[0], cursor_point[1])
            else:
                new_board.put_x(cursor_point[0], cursor_point[1])
            is_player_one = not is_player_one

            if new_board.is_game_over():
                if new_board.is_cats_game():
                    print("Cat's game!")
                elif new_board.is_game_won():
                    player = "player"
                    if is_player_one:
                        player += " 1"
                    else:
                        player += " 2"
                    print("{} wins!".format(player))
                break

    elif cmd == 'exit':
        break
    else:
        print('Unknown command: {}'.format(cmd))

    new_board.print_board(cursor_point)

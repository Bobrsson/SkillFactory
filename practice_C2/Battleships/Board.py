from random import randint


class Point:
    def __init__(self, x, y, if_ships, if_shot):
        self.x = x
        self.y = y
        self.if_ships = if_ships
        self.if_shot = if_shot


class Board:
    def __init__(self, size):
        self.size = size

    board = []

    def generate_board(self, size):
        for x in range(0, size):
            for y in range(0, size):
                print(self.board[i][j], end=' ')
            print()


    for x in range(0, 5):
        board.append(['0' * 5])

    def print_board(board):
        for row in board:
            print(" ".join(row))

    print_board(board)

    def random_row(board):
        return randint(1, len(board))

    def random_col(board):
        return randint(1, len(board[0]))

    ship_row = random_row(board)
    ship_col = random_col(board)

    print(ship_row)
    print(ship_col)

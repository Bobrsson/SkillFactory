from random import randint
import copy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    def __int__(self, length=0, course=0, bow=None, HP=0):
        self.length = length
        self.course = course
        self.bow = bow
        self.hp = HP

    def show_dots(self):
        print(self.bow)

class Board:
    def __init__(self, board='', ships=None, alive=7, hid=True):
        self.board = board
        self.ships = ships
        self.alive = alive
        self.hid = hid

    def add_ship_to_list(self, x):  # Добавляем корабль  в список
        if self.ships is None:
            self.ships = []
        self.ships.extend(x)

    def out(selfs, x, y):
        if (x > 7) or (y > 7):
            return False
        else:
            return True

    def shot(self, cord, hid):
        if hid==True:
            if ==
            self.board[cord[0]][cord[1]] = 'X'
            hidden.board[cord[0]][cord[1]] = 'X'
            return True
        elif self.board[cord1[0]][cord1[1]] == '.' or self.board[cord1[0]][cord1[1]] == 'O':
            self.board[cord1[0]][cord1[1]] = '-'
            hidden.board[cord1[0]][cord1[1]] = '-'
            return False


    def contour(self, x, y, length):  # Обводит корабли контуром
        for i in x.dots:
            if self.board[i[0] - 1][i[1] + 1] == 'O':
                self.board[i[0] - 1][i[1] + 1] = '.'
                y.append((i[0] - 1, i[1] + 1))
            if self.board[i[0]][i[1] + 1] == 'O':
                self.board[i[0]][i[1] + 1] = '.'
                y.append((i[0], i[1] + 1))
            if self.board[i[0] + 1][i[1] + 1] == 'O':
                self.board[i[0] + 1][i[1] + 1] = '.'
                y.append((i[0] + 1, i[1] + 1))
            if self.board[i[0] + 1][i[1]] == 'O':
                self.board[i[0] + 1][i[1]] = '.'
                y.append((i[0] + 1, i[1]))
            if self.board[i[0] + 1][i[1] - 1] == 'O':
                self.board[i[0] + 1][i[1] - 1] = '.'
                y.append((i[0] + 1, i[1] - 1))
            if self.board[i[0]][i[1] - 1] == 'O':
                self.board[i[0]][i[1] - 1] = '.'
                y.append((i[0], i[1] - 1))
            if self.board[i[0] - 1][i[1] - 1] == 'O':
                self.board[i[0] - 1][i[1] - 1] = '.'
                y.append((i[0] - 1, i[1] - 1))
            if self.board[i[0] - 1][i[1]] == 'O':
                self.board[i[0] - 1][i[1]] = '.'
                y.append((i[0] - 1, i[1]))

    def draw_board(self):  # Рисую доску
        for i in range(8):
            for j in range(8):
                print(self.board[i][j], sep=' ')
            print()

    def shot(self, cord1, hidden):  # Отрисовывает результат на поле после хода
        if self.board[cord1[0]][cord1[1]] == 'S':
            self.board[cord1[0]][cord1[1]] = 'X'
            hidden.board[cord1[0]][cord1[1]] = 'X'
            return True
        elif self.board[cord1[0]][cord1[1]] == '.' or self.board[cord1[0]][cord1[1]] == 'O':
            self.board[cord1[0]][cord1[1]] = '-'
            hidden.board[cord1[0]][cord1[1]] = '-'
            return False


    @staticmethod
    def board_new():  # Создает пустое поле
        board = [['O'] * 6 + [' '] for _ in range(6)]
        board = [[' ', '1', '2', '3', '4', '5', '6', ' ']] + board + [[' '] * 8]
        for i in range(1, 7):
            board[i] = list(str(i)) + board[i]
        return board

    def contour(self, x, y):  # Обводит корабли контуром
        for i in x.dots:
            if self.board[i[0] - 1][i[1] + 1] == 'O':
                self.board[i[0] - 1][i[1] + 1] = '.'
                y.append((i[0] - 1, i[1] + 1))
            if self.board[i[0]][i[1] + 1] == 'O':
                self.board[i[0]][i[1] + 1] = '.'
                y.append((i[0], i[1] + 1))
            if self.board[i[0] + 1][i[1] + 1] == 'O':
                self.board[i[0] + 1][i[1] + 1] = '.'
                y.append((i[0] + 1, i[1] + 1))
            if self.board[i[0] + 1][i[1]] == 'O':
                self.board[i[0] + 1][i[1]] = '.'
                y.append((i[0] + 1, i[1]))
            if self.board[i[0] + 1][i[1] - 1] == 'O':
                self.board[i[0] + 1][i[1] - 1] = '.'
                y.append((i[0] + 1, i[1] - 1))
            if self.board[i[0]][i[1] - 1] == 'O':
                self.board[i[0]][i[1] - 1] = '.'
                y.append((i[0], i[1] - 1))
            if self.board[i[0] - 1][i[1] - 1] == 'O':
                self.board[i[0] - 1][i[1] - 1] = '.'
                y.append((i[0] - 1, i[1] - 1))
            if self.board[i[0] - 1][i[1]] == 'O':
                self.board[i[0] - 1][i[1]] = '.'
                y.append((i[0] - 1, i[1]))

    def shot(self, cord1, hidden):  # Отрисовывает результат на поле после хода
        if self.board[cord1[0]][cord1[1]] == 'S':
            self.board[cord1[0]][cord1[1]] = 'X'
            hidden.board[cord1[0]][cord1[1]] = 'X'
            return True
        elif self.board[cord1[0]][cord1[1]] == '.' or self.board[cord1[0]][cord1[1]] == 'O':
            self.board[cord1[0]][cord1[1]] = '-'
            hidden.board[cord1[0]][cord1[1]] = '-'
            return False

board = Board
board.board_new
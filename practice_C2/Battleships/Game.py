class BoardExseption(Exseption):
    pass


class BoardOutExseption(BoardExseption):
    def __str__(self):
        return "Вы пытаетесь выстрелить за достку"


class BoardUsedExseption(BoardExseption):
    def __str__(self):
        return "Вы уже стреляли в эту точку"


class BoardWrongShipsExseption(BoardExseption):
    pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self, other):
        return f"Point({self.x}, {self.y})"

class Ships:
    def __int__(self, length, o, bow):
        self.length = length
        self.o = o
        self.bow = bow
        self.hp = HP
    @property
    def dots(self):
        ships_dots = []
        for i in ranfe(self.length)
            cur_x=self.bow.x
            cur_y=self.bow.y

            if self.o ==0:
                cur_x += i
            elif self.o == 1:
                cur_y += i
            ships_dots.append(Point(cur_x, cur_y))

        return ships_dots

    def shooten (self, shot):
        return shot in self.dots



class Board:
    def __init__(self, size, hid=True):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["0"]*size for in range(size)]

        self.busy = []
        self.ships = []

    def __str__(self):
        res = ""
        res += " | 1 | 2 | 3 | 4 | 5 | 6 |"


from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # это метод который сравнивает точки
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class BoardExseption(Exception):
    pass


class BoardOutExseption(BoardExseption):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску"


class BoardUsedExseption(BoardExseption):
    def __str__(self):
        return "Вы уже стреляли в эту точку"


class BoardWrongShipsExseption(BoardExseption):
    pass


class Ships:
    def __init__(self, bow, length, o):
        self.length = length
        self.o = o
        self.bow = bow
        self.hp = length

    @property  # это метод который возвращает точки корабля
    def dots(self):
        ships_dots = []
        for i in range(self.length):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i
            elif self.o == 1:
                cur_y += i

            ships_dots.append(Point(cur_x, cur_y))

        return ships_dots

    def shooten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, size=6, hid=False):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["0"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "0")
        return res

    def out(self, p):
        return not ((0 <= p.x < self.size) and (0 <= p.y < self.size))

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for p in ship.dots:
            for px, py in near:
                cur = Point(p.x + px, p.y + py)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def add_ship(self, ship):
        for p in ship.dots:
            if self.out(p) or p in self.busy:
                raise BoardWrongShipsExseption()
        for p in ship.dots:
            self.field[p.x][p.y] = "■"
            self.busy.append(p)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, p):
        if self.out(p):
            raise BoardOutExseption
        if p in self.busy:
            raise BoardUsedExseption
        self.busy.append(p)
        for ship in self.ships:
            if p in ship.dots:
                ship.hp -= 1
                self.field[p.x][p.y] = "X"
                if ship.hp == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[p.x][p.y] = "."
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []

    def defeat(self):
        return self.count == len(self.ships)


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardExseption as e:
                print(e)


class AI(Player):
    def ask(self):
        p = Point(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {p.x + 1} {p.y + 1}")
        return p


class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход:").split()
            if len(cords) != 2:
                print("Ввевдите 2 координаты")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print("Введите числа")
                continue

            x, y = int(x), int(y)

            return Point(x - 1, y - 1)


class Game:
    def __init__(self):
        player_board = self.random_board()
        ai_board = self.random_board()
        ai_board.hid = True

        self.ai = AI(ai_board, player_board)
        self.us = User(player_board, ai_board)

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board()
        size = 6
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ships(Point(randint(0, size), randint(0, size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipsExseption:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def print_board(self):
        print("-" * 20)
        print("Доска пользователя:")
        print(self.us.board)
        print("-" * 20)
        print("Доска копухтера:")
        print(self.ai.board)
        print("-" * 20)


    def greet(self):
        print("-------------------")
        print("  Привет  ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def loop(self):
        num = 0
        while True:
            self.print_board()

            if num % 2 == 0:
                repead = self.us.move()
            else:
                repead = self.ai.move()
            if repead:
                num -= 1

            if self.ai.board.defeat():
                self.print_board()
                print("-" * 20)
                print("Вы победили!")
                break

            if self.us.board.defeat():
                self.print_board()
                print("-" * 20)
                print("Вы проиграли!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()

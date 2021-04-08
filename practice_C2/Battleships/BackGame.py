class Point:
    def __init__(self, size=6, hid=False):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["0"] * size for _ in range(size)]
        self.field2 = [["0"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def generat_list(self, field):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |             "
        for i, row in enumerate(field):
            yield f"\n{i+1} | " + " | ".join(row) + " |"

        print(res)

        if self.hid:
            res = res.replace("■", "0")
        return res

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |             "
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "0")
        return res

size=6
field =[["0"] * size for _ in range(size)]
b = Point()
c = str(b.generat_list(field))
print(c)
res = ""
res += "  | 1 | 2 | 3 | 4 | 5 | 6 |             "
for i, row in enumerate(field):
    res += f"\n{i + 1} | " + " | ".join(row) + " |" + b.generat_list(field)
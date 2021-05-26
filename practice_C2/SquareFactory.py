import math
import time
class SquareFactory:
    def __init__(self, a):
        self.a = a

    def ged_side(self):
        return self.a

    @staticmethod
    def get_square():
        return SquareFactory(5)

c=math.trunc(math.fmod(math.fabs(-10000000), 55)+0.3)
print(c)


i=10
while i != 0:
    print(i)
    time.sleep(1)
    i -=1
print("Время")



import random

class SquareFactory:
    def __init__(self, a):
        self.a = a

    def ged_side(self):
        return self.a

    @staticmethod
    def get_square():
        return SquareFactory(5)

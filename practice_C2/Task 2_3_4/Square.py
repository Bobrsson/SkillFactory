class Square:
    _a = None
    def __init__(self, a):
        self.a = a

    @property
    def _size(self):
        return self._size

    @a.setter
    def size(self, value):
        if value > 0:
            self._a = value

    @property
    def get_area_square(self):
        return self.a ** 2

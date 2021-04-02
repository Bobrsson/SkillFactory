class Square:
    def __init__(self, size):
        self.size = size

    @size.setter
    def set_size(self,size):
        if size > 0:
            self.a = size
        elif size == 0:
            raise ValueError("0 не может быть стороной квадрата)")
        else:
            raise ValueError("Длинна стороны должна быть положительна.")

    def get_area_square(self):
        return self.a ** 2

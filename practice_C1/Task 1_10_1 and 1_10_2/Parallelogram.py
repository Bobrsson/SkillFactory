import math


# Класс для Задания 1.10.1
class Parallelogram:
    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle

    def get_area_parallelogram(self):
        return self.a * self.b * math.sin(self.angle % 180)

    # Метод возвращающий строку аргументов класса
    def get_info(self):
        return str('Сторона А: {}. Сторона B: {}. Угол между ними: {}. '.format(self.a, self.b, self.angle))

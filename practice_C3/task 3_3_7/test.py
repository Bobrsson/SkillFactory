import Area


a = int(input('введите сторону ширину'))
b = int(input('введите сторону длинну'))
r = int(input('Введите радиус круга'))
R = Area.area_circle(r)
A = Area.area_square(a, b)
if R > A:
    print('Круг больше!')
else:
    print('Прямоугольник больше!')
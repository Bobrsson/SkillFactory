try:
    a = input('Введите число')
    a = int(a)
except ValueError:
    print('Введите число а не строку')
else:
    print('Вы ввели', a)



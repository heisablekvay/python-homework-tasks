# todo:
#  Создайте класс Triangle с методом, который при создании объекта проверяет три переменный x, y, z на то,
#  что из них можно составить треугольник. Требования: все числа должны быть больше нуля, сумма любых двух должны быть больше третьего.

class Triangle():
    def __init__(self, x, y, z):
        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError('x, y, z > 0 !')

        if (not x + y > z) or (not x + z > y) or (not y + z > x):
            raise ValueError('Сумма двух чисел должна быть больше третьего')


triangle = Triangle(1, 2, 3)
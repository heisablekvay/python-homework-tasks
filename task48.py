# todo:
#  Создайте класс Shape, объекты которого имеют атрибуты
#  Colour – строка, например, «Красный», «Синий»;
#  Square – площадь объекта.
#  Создайте несколько методов:
#  1) Установить цвет объекта.
#  2) Запросить цвет объекта и напечатать его.
#  3) Задать площадь объекта.
#  4) Запросить площадь  объекта.

class Shape:
    def __init__(self, Color, Square):
        self.__color = Color
        self.__square = Square

    @property
    def color(self):
        print(f'Цвет объекта: {self.__color}')
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, square):
        self.__square = square


obj = Shape('Red', 40)
print(obj.color + ' ' + str(obj.square))

obj.color = 'Green'
print(obj.color + ' ' + str(obj.square))

obj.square = 50
print(obj.color + ' ' + str(obj.square))


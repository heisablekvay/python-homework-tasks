# todo: Создать абстрактный класс Press (пресса) содержащий:
# Поля: название, цена за единицу.
# В классе должны быть абстрактные методы:
# метод SetPrice (без параметров) – установка цены.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Magazine - журнал,
# Book- книга.

from abc import ABC, abstractmethod


class Press(ABC):
    name = ''
    price = 0

    @abstractmethod
    def SetPrice(self):
        pass

    @abstractmethod
    def Info(self):
        pass


class Magazine(Press):
    name = 'журнал'

    def SetPrice(self, price):
        self.price = price

    def Info(self):
        print(f'{self.name.capitalize()} стоит {self.price}$')


class Book(Press):
    name = 'книга'

    def SetPrice(self, price):
        self.price = price

    def Info(self):
        print(f'{self.name.capitalize()} стоит {self.price}$')


magazine = Magazine()
book = Book()

magazine.SetPrice(50)
book.SetPrice(100)

magazine.Info()
book.Info()

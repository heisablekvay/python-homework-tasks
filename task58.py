# todo: Создать абстрактный класс Transport (транспорт) содержащий:
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.

from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self):
        self.__price = None
        self.__speed = None
        self.__self_price = None

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    @abstractmethod
    def speed(self, val):
        self.__speed = val

    @property
    def self_price(self):
        return self.__self_price

    @self_price.setter
    @abstractmethod
    def self_price(self, val):
        self.__self_price = val

    @property
    def price(self):
        return self.__price

    @price.setter
    @abstractmethod
    def price(self, val):
        self.__price = val

    @abstractmethod
    def Cost(self):
        return self.__price + self.self_price

    @abstractmethod
    def Info(self):
        return f'Тип транспорта. Скорость = {self.speed}, себестоимость = {self.self_price}, стоимость = {self.price}'


class Marine(Transport):
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val):
        self.__speed = val

    @property
    def self_price(self):
        return self.__self_price

    @self_price.setter
    def self_price(self, val):
        self.__self_price = val

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val

    def Cost(self):
        return self.price + self.self_price

    def Info(self):
        return f'Морской. Скорость = {self.speed}, себестоимость = {self.self_price}, стоимость = {self.price}'

    def __init__(self, speed, self_price, price):
        self.__speed = speed
        self.__self_price = self_price
        self.__price = price


class Ground(Transport):
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, val):
        self.__speed = val

    @property
    def self_price(self):
        return self.__self_price

    @self_price.setter
    def self_price(self, val):
        self.__self_price = val

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val

    def Cost(self):
        return self.price + self.self_price

    def Info(self):
        return f'Наземный. Скорость = {self.speed}, себестоимость = {self.self_price}, стоимость = {self.price}'

    def __init__(self, speed, self_price, price):
        self.speed = speed
        self.self_price = self_price
        self.price = price


# Я правильно понял, что каждый метод, в том числе поле (определенное у меня через геттер и сеттер) должно быть
# переопределено в дочернем классе? Просто возникает какое-то жуткое дублирование кода. Как-то можно эту проблему
# решить?
marine = Marine(50, 100, 200)
print(marine.Info())

ground = Ground(50, 100, 200)
print(ground.Info())


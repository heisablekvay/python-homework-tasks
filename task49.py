# todo:
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.

class Person:
    def __init__(self, surname, age):
        self.__surname = surname
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        pass


person = Person('Иванов', 29)
print(person.age)

person.age = 42
print(person.age)

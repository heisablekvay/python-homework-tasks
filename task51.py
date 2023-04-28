#todo:
# Определите класс Person. При создании объекта p=Person(‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ

class Person:
    def __init__(self, last_name, first_name, patronymic):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic

    def __str__(self):
        return self.patronymic[::-1] + \
            self.last_name[::-1] + \
            self.first_name[::-1]


human = Person('Иванов', 'Михаил', 'Федорович')
print(human)

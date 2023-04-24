# todo:
#   Создайте класс Pet с атрибутам имя, вес и уровень сытости.
#   Напишите метод info, который в качестве результата выдает эти атрибуты.
#   Напишите метод hungry, который возвращает уровень сытости и комментирует: если меньше 5, то «голоден», если больше 10, то «сыт».
#   Напишите метод feed, который передает питомцу некоторую еду, которая прибавляется к уровню сытости и вызывает метод info.


class Pet:
    def __init__(self, name, weight, hungry_lvl):
        self.name = name
        self.weight = weight
        self.hungry_lvl = hungry_lvl

    def info(self):
        print(f'{self.name} весит {self.weight}. Голодный на {self.hungry_lvl}%')

    def hungry(self):
        if self.hungry_lvl < 5:
            print('Голоден')
        elif self.hungry_lvl > 10:
            print('Сыт')

        return self.hungry_lvl

    def feed(self, food):
        self.hungry_lvl += food
        self.info()


pet = Pet('Осел', 50, 4)

pet.hungry()
pet.feed(3)
pet.feed(3)

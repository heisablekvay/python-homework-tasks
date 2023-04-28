# todo:
#  Разработать систему учета решения задач учениками курса «Разработчик на Питоне».
#
# Проблема.
# Преподаватель каждый урок задает некоторое количество задач в качестве домашнего задания, для упрощения можно считать, что одну.
# Каждый ученик решает каждую задачу. Переводит ее статус в решенную.
# Преподаватель проверяет каждую задачу каждого ученика и либо подтверждает ее статус как решенную или меняет ее статус как не решенную.
# Вопрос. Как спроектировать систему классов на Питоне для решения задачи учета?
# Разработайте систему
# классов (Teacher, Pupil, Lesson, Task. Нужен ли класс Группа?);
# атрибутов для каждого состояния каждого объекта;
# методов для каждого объекта.
# Отчетность? Запросы? Начните с формулировки решаемой задачи – спецификации или технического задания. Затем спроектируйте классы, атрибуты, методы. Протестируйте систему.

import random


class Task:
    done_flag = False

    def complete(self):
        self.done_flag = True

    def incomplete(self):
        self.done_flag = False


class Lesson:
    def __init__(self):
        self.__tasks = None

    @property
    def tasks(self):
        return self.__tasks

    @tasks.setter
    def tasks(self, tasks):
        self.__tasks = tasks


class Pupil:
    def __init__(self):
        self.homework = []

    def add_homework(self, task):
        self.homework.append(task)


class Teacher:
    @staticmethod
    def give_homework(lesson, group):
        home_task_num = random.randint(1, 3)
        tasks = [Task() for _ in range(home_task_num)]
        lesson.tasks = tasks
        for pupil in group:
            for task in tasks:
                pupil.add_homework(task)

    @staticmethod
    def check_task(task):
        task.complete()

    def check_pupil_homework(self, pupil):
        for task in pupil.homework:
            self.check_task(task)

    def check_group_homework(self, group):
        for pupil in group:
            self.check_pupil_homework(pupil)


def print_pupils(pupils):
    pn = 1
    for pupil in pupils:
        tn = 1
        for task in pupil.homework:
            print(f'Pupil #{pn}: task #{tn}: status = {task.done_flag}')
            tn += 1
        pn += 1


teacher = Teacher()

pupil_num = 6
pupils = [Pupil() for _ in range(pupil_num)]

lesson1 = Lesson()
teacher.give_homework(lesson1, pupils)

print_pupils(pupils)

teacher.check_group_homework(pupils)
print_pupils(pupils)

# todo:
#  Функция get_weekday()
#  Реализуйте функцию get_weekday(), которая принимает один аргумент:
#
#  number — целое число (от 1 до 7 включительно)
#  Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:
#
#  если number не является целым числом, функция должна возбуждать исключение:
#  TypeError('Аргумент не является целым числом')
#  если number является целым числом, но не принадлежит отрезку [1;7]
#  функция должна возбуждать исключение:
#  ValueError('Аргумент не принадлежит требуемому диапазону')
# todo:
# Сделайте функцию get_weekday() статической в классе Helper


week = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday'
}


class Helper:
    @staticmethod
    def get_weekday(number):
        if not isinstance(number, int):
            raise TypeError('Аргумент не является целым числом')
        if not (1 <= number <= 7):
            raise ValueError('Аргумент не принадлежит требуемому диапазону')

        global week
        return week[number]


try:
    print(Helper.get_weekday(1))
except Exception as e:
    print(Exception, e)


# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.

def sumn(number):
    return number + sumn(number - 1) if number else 0


number = int(input('Введите число: '))

print(sumn(number))
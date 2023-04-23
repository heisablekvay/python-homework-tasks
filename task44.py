#todo: Напишите программу, в которой используется две функции. В одной программа «спит» 2 секунды, в другой – 3 секунды.
# Пусть каждая функция возвращает время, которое она «проспала». Главная программа запускает цикл от 0 до 10, если число
# четное, то запускает функцию с 2 секундами, если нечетное, то функцию с 3 секундами.
# Накапливает сон обеих функций отдельно и печатает две суммы.

from time import sleep


def sleep_2sec():
    sleep(2)
    return 2


def sleep_3sec():
    sleep(3)
    return 3


sleep_odd = 0
sleep_even = 0

for num in range(11):
    if num % 2 == 0:
        sleep_even += sleep_2sec()
    else:
        sleep_odd += sleep_3sec()

print(f'Sleep 2 sec total: {sleep_even}')
print(f'Sleep 3 sec total: {sleep_odd}')


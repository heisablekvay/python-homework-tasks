# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.

from calendar import monthrange


def get_month_numbers(year, month):
    return [number for number in range(1, (monthrange(year, month))[1] + 1)]


print(get_month_numbers(2023, 4))
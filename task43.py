# todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.

import calendar

year = 2023
total_months = 12
third_thursdat_idx = 2

c = calendar.Calendar(firstweekday=calendar.MONDAY)
for month in range(1, total_months + 1):
    monthcal = c.monthdatescalendar(year, month)
    third_thursdays = [day for week in monthcal for day in week if
                       day.weekday() == calendar.THURSDAY and day.month == month][third_thursdat_idx]
    print(third_thursdays)

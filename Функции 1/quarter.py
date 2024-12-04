# -*- coding: utf-8 -*-
def quarter(numbers):
    numbers = numbers.split(';')
    x = float(numbers[0])
    y = float(numbers[1])
    if x > 0 and y > 0:
        print('I четверть')
    elif x < 0 and y > 0:
        print('II четверть')
    elif x < 0 and y < 0:
        print('III четверть')
    elif x > 0 and y < 0:
        print('IV четверть')
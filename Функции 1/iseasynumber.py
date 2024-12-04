# -*- coding: utf-8 -*-
def Prime(number):
    d = 0
    for i in range(1, number+1):
        if number % i == 0:
            d+=1
    if d > 2:
        print('Составное число')
    else:
        print('Простое число')
#-*- coding: utf-8 -*- 
from random import choice
r = [i/10 for i in range(0, 20)]
square, circle = 1, 1 ;"""Стороны квадрата и окружности"""
points = [(choice(r), choice(r)) for _ in range(100000)] ;"""Случайно сгенерированные точки"""
square_count, circle_count = 0, 0 ;"""Колличество попаданий в окружность"""
for (x, y) in points:
    if x**2 + y **2 >= circle**2: square_count += 1
    else: circle_count += 1
pi = (square_count/ (circle_count+square_count))*4 ;"""Число ПИ есть отношение точек, попавших в круг к общему их колличеству"""
print(pi)

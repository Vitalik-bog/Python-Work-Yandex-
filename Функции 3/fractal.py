#-*-coding: utf8 -*-
fractal = [0, [], [], 2]
def fractalling():
    global fractal
    fractal[1] = fractal ;"""Меняем список списка, присваивая ему значение самого глобального списка"""
    fractal[2] = fractal ;"""Меняем список списка, присваивая ему значение самого глобального списка"""
fractalling()
#print(fractal)

   

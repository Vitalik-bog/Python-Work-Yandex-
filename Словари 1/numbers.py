# -*- coding: utf-8 -*-
numbers, result = {}, []
for i in range(int(input())):
    data = input().split()
    if not data[1] in numbers: numbers.update({data[1]:data[0]})
    else: numbers.update({data[1]:numbers[data[1]] + ' ' + data[0]})
for i in range(int(input())): 
    name = input()
    if name in numbers: result.append(numbers[name])
    else: result.append('Нет в телефонной книге')
[print(res) for res in result]
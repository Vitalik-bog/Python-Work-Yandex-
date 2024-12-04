# -*- coding: utf-8 -*-
count, olga, sasha = int(input()), {}, {}
for _ in range(count):
    data = input().split()
    sasha.update({data[0]:sum([int(i) for i in data[1:]])/len(data[1:])})
for _ in range(count):
    data = input().split()
    olga.update({data[0]:sum([int(i) for i in data[1:]])/len(data[1:])})
results = []
for subject, mark in sasha.items():
    if sasha[subject] == olga[subject]: results.append(subject + " ничья")
    elif sasha[subject] < olga[subject]: results.append(subject + " Оля")
    elif sasha[subject] > olga[subject]: results.append(subject + " Саша")
[print(item) for item in sorted(results)]
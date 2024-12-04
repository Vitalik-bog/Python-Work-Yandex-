# -*- coding: utf-8 -*-
n, main = int(input()), input().split(" опубликовал пост, количество просмотров: ")
scores = {main[0]:int(main[1])}
for i in range(n-1):
    data = input()
    name, fr, score = data.split(' отрепостил пост у ')[0], data.split(', количество просмотров: ')[0].split(' отрепостил пост у ')[-1], int(data.split(', количество просмотров: ')[-1])
    if not name in scores: scores.update({name: score})
    else: scores.update({name: scores[name]+score})
    scores.update({fr: scores[fr]+score})
[print(score) for score in scores.values()]
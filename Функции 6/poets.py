# -*- coding: utf-8 -*-
 
def checkpoet(poet):
    Vowels, results, phrases = ('а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я'), [], poet.split()
    [results.append(len([i for i in range(len(phrase)) if phrase[i] in Vowels])) for phrase in phrases]
    if bool(results) and sum(results)/len(results) == results[0]: print('Парам пам-пам')
    else: print('Пам парам')
checkpoet(input())
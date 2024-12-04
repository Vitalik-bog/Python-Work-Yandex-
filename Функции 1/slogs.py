# -*- coding: utf-8 -*-
def printLongWords(text):
    words = []
    word = ''
    for i in range(len(text)):
        if text[i].isalpha():
            word += text[i]
        if (not(text[i].isalpha()) or i+1 == len(text)) and word != '':
            words += [word]
            word = ''
    for w in words:
        c = 0
        for j in list(w):
            if j in ['а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я'] or j in ['a', 'e', 'i', 'o', 'u']:
                c += 1
        if c >= 4:
            print(w.lower())
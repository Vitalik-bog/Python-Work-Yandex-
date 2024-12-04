#-*- coding: utf-8 -*- 
from swift import words
from random import choice
text, count = ' ', int(input('Колличество предложений: '))
current = words[3096]
while text.count('.') < count:
    text += current+' '
    variants = [words[word+1] for word in range(len(words[:-1])) if words[word] == current]
    current = choice(variants)
print(text[1:])
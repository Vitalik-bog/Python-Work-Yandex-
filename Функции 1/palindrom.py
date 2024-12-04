# -*- coding: utf-8 -*-
def Palindrome(line):
    l = line
    line = list(line)
    line.reverse()
    line = ''.join(line)
    if l.replace(' ', '').lower() == ''.join(line).replace(' ', '').lower():
        print('Палиндром')
    else:
        print('Не палиндром')

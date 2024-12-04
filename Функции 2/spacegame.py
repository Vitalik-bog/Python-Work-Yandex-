#-*-coding: utf8 -*-
def spaceGame(text):
    if text.count(' ') % 2 == 0:
        print('Вы выиграли')
    else:
        print('Вы проиграли')
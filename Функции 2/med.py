#-*-coding: utf8 -*-
base = []

def hello(name):
    print('Здравствуйте,',name+'!', 'Вашу карту ищут...')

def searchCard(name):
    global base
    for i in range(len(base)):
        if base[i] == name:
            print('Ваша карта с номером', i+1, 'найдена')
            return True
    print('Ваша карта не найдена')
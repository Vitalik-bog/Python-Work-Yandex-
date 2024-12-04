# -*- coding: utf-8 -*-
def askPassword():
    res = ''
    c = 0
    while True:
        password = input()
        c+=1
        if password == 'password' and c <= 3 and res != 'success':
            res = 'success'
            print('Пароль принят')
            break
        if c >= 3 and res == '':
            print('В доступе отказано')
            res = 'forbidden'
            break
# -*- coding: utf-8 -*-
def print_document(pages):
    secret = False
    for page in pages: 
        if not 'Секретно' in page: print(page)
        else: 
            secret = True
            break
    if not secret: print('Напечатано без купюр')
    else: print('Дальнейшие материалы засекречены')
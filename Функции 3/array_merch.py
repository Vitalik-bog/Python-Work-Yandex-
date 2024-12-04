#-*-coding: utf8 -*-
"""
Пример 1. Категорически не заменяют друг друга.

Реализовано подобие покупки в магазине. Переиенна cart - корзина, check - итоговый чек.
В идеальных условиях они должны быть одинаковы. Но...

cart += [product] - изменяет текущий объект, не "ломая" связей.
cart = cart + [product] - инициирует появление нового объекта. Перменные cart и check становятся независимыми друг от друга.

"""

cart = check = []

def addToCart(product):
    global cart
    cart += [product]
    
def addToCart__INVALID(product): # Неверная реализация
    global cart
    cart = cart + [product]

def getProductsOnCart():
    print(cart)
    
def printCheck():
    print(check)
    
print('-------------------\nПример 1.')

addToCart('product')
getProductsOnCart()
printCheck()

addToCart__INVALID('product_2')
getProductsOnCart()
printCheck()

"""

Пример 2. Могут быть заменены друг другом. Результат не изменится.
Реализована функция хранения стека паролей.

"""
print('-------------------\nПример 2.')
def add(password):
    global passwords
    passwords += [password]
    
def add_2(password):
    global passwords
    passwords = passwords + [password]
    
passwords = []
add('qwerty')
add_2('1234')
print(passwords)
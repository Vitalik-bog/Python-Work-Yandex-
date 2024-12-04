# -*- coding: utf-8 -*-

"""
main() - Главный посредник всех функций, диалог с пользователем
getCountData() - Счётчик быков и коров
isset() - Проверка корректности нового числа

Низкоуровневые функции:
numberToArray()
arrayToNumber()

"""

import random
def main():
    name, history, answer = input("Ваше имя: "), [], None
    print('Добро пожаловать в игру "Коровы и быки,"', name, "!")
    secret = random.randint(1000, 9999)
    while True:
        #print(secret)
        answer = int(input(name+ ", ваше число: "))
        res = getCountData(numberToArray(secret), numberToArray(answer))
        if res[1] >= 2:
            secret = random.randint(1000, 9999)
            while isset(secret, history): secret = random.randint(1000, 9999)
        print("Быки:", res[1], "Коровы:", res[2])
        history.append(res)
    print('\n****************************************************************\n')
    print('Вы выиграли, можете гордиться! Вы только что обманули обманщика!')
        
    
def getCountData(number1, number2):
    bulls, cows = 0, 0
    for numeral in range(4):
        if number1[numeral] == number2[numeral]: bulls += 1
        if str(number1[numeral]) in str(number2): cows += 1
    return (arrayToNumber(number2), bulls, cows)

def isset(number, history):
    for answer in history:
        if number in answer: return True
    return False

def numberToArray(number):
    return list(str(number))

def arrayToNumber(array):
    return int(''.join(array.copy()))
    
main()
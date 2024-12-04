#-*-coding: utf8 -*-

GameArea = False

def start(): #ГЛАВНАЯ ФУНКЦИЯ ЗАПУСКА ИГРЫ
    global GameArea
    init()
    while checkEndtheGame(GameArea) and whoWin(GameArea) == 'draw':
        printgame()
        correctGame(GameArea, setstep(GameArea))
    printgame()
    if whoWin(GameArea) == 'x':
        print('Поздравляем! Победитель - x')
    elif whoWin(GameArea) == '0':
        print('Поздравляем! Победитель - 0')
    else:
        print('Поздравляем! Дружеская ничья!')

def init():
    global GameArea
    GameArea = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
def printgame():
    for line in GameArea:
        string = ''
        for symbol in range(len(line)):
            if symbol == 0:
                string += ' ' + line[symbol] + ' '
            else:
                string += '| '+ line[symbol] + ' '
        print(string)
        print(' -- --- --')
def setstep(array):
    step = input('Очередной ход (через пробел - поочерёдно каждая из координат и символ): ').split()
    while array[int(step[0])][int(step[1])] != ' ' or (step[2] != 'x' and step[2] != '0'):
        step = input('Введите корректный ход (через пробел - поочерёдно каждая из координат и символ): ').split()
    return step
        
def correctGame(array, change):
    array[int(change[0])][int(change[1])] = change[2]
    
def checkEndtheGame(array):
    for i in array:
        if ' ' in i:
            return True
    return False
    
def whoWin(array):
    lines = [''.join(i) for i in array]
    win = 'draw'
    for line in lines:
        if 'xxx' in line:
            win ='x'
            break
        if '000' in line:
            win = '0'
            break
    if win == 'draw':
        for j in range(3):
            if lines[0][j] == 'x' and lines[1][j] == 'x' and lines[2][j] == 'x':
                win = 'x'
            elif lines[0][j] == '0' and lines[1][j] == '0' and lines[2][j] == '0':
                win = '0'
    if win == 'draw':
        if lines[0][0] == 'x' and lines[1][1] == 'x' and lines[2][2] == 'x':
            win = 'x'
        elif lines[0][2] == 'x' and lines[1][1] == 'x' and lines[2][0] == 'x':
            win = 'x'
    if win == 'draw':
        if lines[0][0] == '0' and lines[1][1] == '0' and lines[2][2] == '0':
            win = '0'
        elif lines[0][2] == '0' and lines[1][1] == '0' and lines[2][0] == '0':
            win = '0'        
    return win

start()
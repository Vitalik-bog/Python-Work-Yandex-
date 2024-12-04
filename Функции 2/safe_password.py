#-*-coding: utf8 -*-

def checkPin(pinCode):
    code = pinCode.split('-')
    if iseasy(int(code[0])) and isPalendrome(str(code[1])) and check2rec(int(code[2])):
        print('Корректен')
    else:
        print('Некорректен')
    
def iseasy(n):
    d = 0
    for i in range(1, n+1):
        if n % i == 0:
            d += 1
    if d != 2:
        return False
    return True
    
def isPalendrome(data):
    data, d = list(data), data
    data.reverse()
    if ''.join(d) == ''.join(data):
        return True
    return False
def check2rec(num):
    if num == 0:
        return True
    if num == 1:
        return True
    if num & 1:
        return False
    return check2rec(num >> 1)

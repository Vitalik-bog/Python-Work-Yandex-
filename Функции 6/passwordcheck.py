# -*- coding: utf-8 -*-
def main():
    result = askPassword(retResults, retResults)
    if len(result) == 1: print('Привет,', result[0]+'!')
    else: print('Кто-то пытался притвориться пользователем', result[0]+',', 'но в пароле допустил ошибку:', result[1].upper()+'.')
        

def askPassword(success, failure):
    login, password = input(), input()
    Vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    Consonant = [i for i in list(login) if not i in Vowels]
    input_vowels, input_consonant = [symbol for symbol in password if symbol in Vowels], [symbol for symbol in password if symbol not in Vowels]
    if len(input_vowels) != 3 and list(input_consonant) != Consonant:
        return failure(login, 'Everything is wrong')
    elif len(input_vowels) != 3:
        return failure(login, 'Wrong number of vowels')
    elif list(input_consonant) != Consonant:
        return failure(login, 'Wrong consonants')
    return success(login)

def retResults(*args):
    return [arg for arg in args]

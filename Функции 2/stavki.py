#-*-coding: utf8 -*-
bets = {}

def doBet(horse, bet):
    global bets
    if bets.get(horse) or bet <= 0 or horse > 10 or horse <= 0:
        print('Что-то пошло не так, попробуйте еще раз')
        return False
    bets.update({horse:bet})
    print('Ваша ставка в размере', bet, 'на лошадь', horse, 'принята')

#-*-coding: utf8 -*-
Object = False

def setupProfile(name, vacationDates):
    global Object
    Object = (name, vacationDates)
    
def printApplicationForLeave():
    global Object
    print('Заявление на отпуск в период', Object[1] + '.', Object[0])
    
def printHolidayMoneyClaim(amount):
    print('Прошу выплатить', amount, 'отпускных денег.', Object[0])

def printAttorneyLetter(toWhom):
    print('На время отпуска в период', Object[1], 'моим заместителем назначается', toWhom+'.', Object[0])

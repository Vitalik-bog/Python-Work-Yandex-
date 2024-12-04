#-*-coding: utf8 -*-
lastTicket = ''

def lucky(ticket):
    global lastTicket
    if checkTicket(lastTicket) and checkTicket(ticket):
        print('Счастливый')
    else:
        print('Несчастливый')
    lastTicket = ticket
def checkTicket(ticket):
    ticket = str(ticket)
    while len(ticket) < 6:
        ticket = '0' + ticket
    if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5]):
        return True
    return False
# -*- coding: utf-8 -*-
def Late(thistime, starttime, busestime):
    thistime = [int(i) for i in thistime.split(':')]
    starttime = [int(i) for i in starttime.split(':')]
    thistime = thistime[0]*60 + thistime[1]
    starttime = starttime[0]*60 + starttime[1]
    #busestime = [int(i) for i in busestime.split()]
    late = True
    while late and len(busestime) != 0:
        if thistime+5 <= thistime + max(busestime) and thistime + 15 + max(busestime) <= starttime:
            late = max(busestime)
            break
        else:
            del busestime[busestime.index(max(busestime))]
    if late != True:
        print('Выйти через',late-5,'минут')
    else:
        print('Опоздание')

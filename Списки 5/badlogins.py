#-*-coding: utf8 -*-
passwords = [i for i in input().split(',')]
valid = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбюQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890_'
out = []
for pas in passwords:
    for i in range(len(pas)):
        if not pas[i] in valid:
            out += [pas]
            break
out.sort()
for i in out:
    if len(i) < len(max(out, key=len)):
        i = i.rjust(len(max(out, key=len)), ' ')
    print(i)
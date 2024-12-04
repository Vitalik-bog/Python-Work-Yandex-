#-*-coding: utf8 -*-
commands = [input() for i in range(int(input()))]
course = []
out = []
for comand in commands:
    
    if 'Кто последний?' in comand:
        course += [comand[19:-1]]
    elif 'Я только спросить!' in comand:
        course.insert(0, comand[23:-1])
    elif 'Следующий!' in comand:
        if course:
            out += ['Заходит ' + course[0] + '!']
            course = course[1:]
        else:
            out += ['В очереди никого нет.']
for i in out:
    print(i)
#-*-coding: utf8 -*-
commands = [input() for i in range(int(input()))]
course = []
for do in commands:
    if ' встала в очередь.' in do or ' встал в очередь.' in do:
        course += [do[:-17].strip()]
    elif 'Привет, ' in do and ' будет за тобой.' in do:
        do = do[8:-16]
        course.insert(course.index(do.split('!')[0].strip())+1, do.split('!')[1].strip())
    elif ', хватит тут стоять, пошли отсюда.' in do:
        del course[course.index(do[:-34])]
for p in course:
    print(p)
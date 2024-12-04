import random

stones = int(input())
datastones = False
userstones = False
while stones != 0:
    datastones = random.randint(1, 3)
    while datastones > stones or datastones < 1:
        datastones = random.randint(1, 3)
    stones = stones - datastones
    print('Программой взято', datastones, 'камня(ей)', 'осталось', stones, 'камня(ей)')
    if stones == 0:
        print('Выиграл исскуственный интеллект Алексея Медведева. Поздравляем с проигрышем!')
    else:
        userstones = int(input())
        while userstones < 1 or userstones > 3 or userstones > stones:
            userstones = int(input())
        stones = stones - userstones
        print('Пользователем взято', userstones, 'камня(ей)', 'осталось', stones, 'камня(ей)')
        if stones == 0:
            print('Как это не странно, но вы выиграли!')
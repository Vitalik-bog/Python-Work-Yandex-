import random
heap = int(input())
progress = 'mashine'
stones = False
while heap > 0:
    while progress == 'mashine':
        stones = random.randint(1, 3)
        while stones > heap:
            stones = random.randint(1, 3)
        heap -= stones
        print('Компьютер взял', stones, 'камней. Осталось', heap, 'камней')
        stones = 0
        progress = 'user'
    if heap == 0:
        break
    while progress == 'user':
        stones = int(input())
        while stones > 3 or stones > heap or stones <= 0:
            stones = int(input())
        heap -= stones
        print('Пользователь взял', stones, 'камней. Осталось', heap, 'камней')
        progress = 'mashine'
if progress == 'mashine':
    print('Жаль, но вы проиграли! Эй ребята, опишите его имущество!')
else:
    print('Вы чего, неужели выиграли? Но этого же не может быть!')
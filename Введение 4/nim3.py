import random
heap_1 = int(input())
heap_2 = int(input())
heap_3 = int(input())
progress = 'mashine'
stones = False
while heap_2 > 0 or heap_1 > 0 or heap_3 > 0:
    while (progress == 'mashine') and (heap_1 > 0 or heap_2 > 0 or heap_3 > 0):
        heap = random.randint(1, 3)
        if heap_1 == 0:
            heap = random.randint(2, 3)
        elif heap_2 == 0:
            heap = random.randint(1, 3)
        elif heap_3 == 0:
            heap = random.randint(1, 2)        
        if heap == 1:
            stones = random.randint(1, heap_1)
            while stones > heap_1:
                stones = random.randint(1, heap_1)
            heap_1 -= stones
        elif heap == 2:
            stones = random.randint(1, heap_2)
            while stones > heap_2:
                stones = random.randint(1, heap_2)
            heap_2 -= stones
        else:
            stones = random.randint(1, heap_3)
            while stones > heap_3:
                stones = random.randint(1, heap_3)
            heap_3 -= stones
        print('Компьютер взял', stones, 'камней из кучи под номером', heap)        
        print(heap_1, heap_2, heap_3)
        progress = 'user'
    stones = 0
    while (progress == 'user') and (heap_1 > 0 or heap_2 > 0 or heap_3 > 0):
        heap = int(input())
        if heap == 1:
            stones = int(input())
            while stones > heap_1:
                stones = int(input())
            heap_1 -= stones
        elif heap == 2:
            stones = int(input())
            while stones > heap_2:
                stones = int(input())
            heap_2 -= stones
        elif heap == 3:
            stones = int(input())
            while stones > heap_3:
                stones = int(input())
            heap_3 -= stones        
        print('Пользователь взял', stones, 'камней из кучи под номером', heap)
        print(heap_1, heap_2, heap_3)
        progress = 'mashine'
if progress == 'user':
    print('Жаль, но вы проиграли! Эй ребята, снимите-ка с него шкуру!')
else:
    print('Вы чего, опять выиграли? Но этого же не может быть!')
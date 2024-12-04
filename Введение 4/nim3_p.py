heap_1 = int(input())
heap_2 = int(input())
heap_3 = int(input())
stones = False
while heap_1 > 0 or heap_2 > 0 or heap_3 > 0:
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
    print(heap_1, heap_2, heap_3)
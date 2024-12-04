stones = int(input())
while stones != 0:
    progress = int(input())
    if progress >= 1 and progress <= 3 and progress <= stones:
        stones = stones - progress
    print(stones)
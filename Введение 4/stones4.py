stoneplace_1 = int(input())
stoneplace_2 = int(input())
userplace = False
while stoneplace_1 + stoneplace_2 != 0:
        userplace = int(input())
        if userplace == 1:  
                userstone = int(input())
                stoneplace_1 -= userstone
                print(stoneplace_1, stoneplace_2)
        elif userplace == 2:
                userstone = int(input())
                stoneplace_2 -= userstone
                print(stoneplace_1, stoneplace_2)
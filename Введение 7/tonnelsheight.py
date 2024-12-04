res_height = 0
res_road = 0
final_height = 0
final_road = 0
roads = int(input())
for i in range(1, roads+1):
    tonnels = int(input())
    for j in range(1, tonnels+1):
        height = int(input())
        if j==1:
            res_road = i
            res_height = height
        if res_road == i and height < res_height:
            res_height = height
            res_road = i
    if res_height > final_height:
        final_height = res_height
        final_road = res_road
print(final_road, final_height)
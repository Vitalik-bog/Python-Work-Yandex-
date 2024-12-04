days = 0
temp = 0
while temp < 22.0:
    temp = float(input())
    if temp < 22.0:
        days += 1
print(days // 7)
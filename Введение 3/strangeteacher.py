money = int(input())
res = 0
while money >= 8:
    modulo = money % 8
    if modulo == 0 or modulo < 8:
        modulo = ''
    money = money // 8
    res = str(money) + str(modulo)
print(res)

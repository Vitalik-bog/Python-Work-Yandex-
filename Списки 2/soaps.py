dishes = ('щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански')
n = int(input())
j = 0
for i in range(n):
    print(dishes[j])
    j+=1
    if j == len(dishes):
        j = 0
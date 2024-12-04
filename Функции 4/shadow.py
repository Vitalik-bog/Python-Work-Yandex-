# -*- coding: utf-8 -*-
def main():
    k, lane = int(input()), input().split()
    #print(makeShades(lane, k))
    if calculateSunnyLength(makeShades(lane, k)) >= 10: print('Обгорел')
    else: print('Тени достаточно')
    
def makeShades(alley, k):
    if k < 0: alley.reverse()
    result = [[] for e in alley]
    for step in alley:
        if int(step) > 0:
            if k != 0: end = (alley.index(step)+int(step))*abs(k)
            else: end = alley.index(step)+1
            while end > len(result): end-=1
            for i in range(alley.index(step), end):
                result[i] = [True]
                if i+1 != len(result) and k != 0: result[i+1] = [True]
    for el in result: 
        if el == []: el += [False]
    result = [i[0] for i in result]
    if k < 0: result.reverse()
    return result

def calculateSunnyLength(shades):
    res = 0
    for shade in shades:
        if shade == False: res += 1
    return res
#main()
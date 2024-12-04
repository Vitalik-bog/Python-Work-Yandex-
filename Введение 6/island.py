hoard = [int(input()), int(input())]
user = [0, 0]
i = 0
steps_final = 0
side = input()
while side != 'стоп':
    i +=1
    step = int(input())
    if side == 'север':
        user[1] += step
    elif side == 'юг':
        user[1] -= step
    elif side == 'восток':
        user[0] += step
    elif side == 'запад':
        user[0] -= step
    if user == hoard and steps_final == 0:
        steps_final = i
    side = input()    
print(steps_final)


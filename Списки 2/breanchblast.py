comands = input()
lent = []
for i in range(30001):
    lent += [0]
position = 0
this = lent[position]
for i in range(len(comands)):
    this = lent[position]
    if comands[i] == '+':
        if this == 255:
            lent[position] = 0
        else:
            lent[position] += 1
    elif comands[i] == '-':
        if this == 0:
            lent[position] = 255
        else:
            lent[position] -= 1
    elif comands[i] == '>':
        if position == 30000:
            position = 0
        else:
            position += 1
    elif comands[i] == '<':
        if position == 0:
            position = 30000
        else:
            position -= 1
    elif comands[i] == '.':
        print(this)

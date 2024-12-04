string = input()
order = []
symbol = string[0]
count = 0
for i in range(len(string)):
    if string[i] == symbol:
        count += 1
        if i == len(string)-1:
            order += [[count, symbol]]        
    else:
        order += [[count, symbol]]
        symbol = string[i]
        count = 1
        if i == len(string)-1:
            order += [[count, symbol]]
for i in range(len(order)):
    for j in range(len(order[i])):
        print(order[i][j], ' ', end='')
    print()
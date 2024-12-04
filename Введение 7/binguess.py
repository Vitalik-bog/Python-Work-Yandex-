numrange = [0, 1000]
variant = False
for i in range(10):
    variant = (numrange[1] + numrange[0])/2
    print(int(variant))
    check = input()
    if check == "=":
        break
    elif check == '>':
        numrange[1] = variant
        if (numrange[1] + numrange[0])%2 != 0:
            numrange[1] = variant + 1
        continue
    elif check == '<':
        numrange[0] = variant
        if (numrange[1] + numrange[0])%2 != 0:
            numrange[0] = variant + 1        
        continue
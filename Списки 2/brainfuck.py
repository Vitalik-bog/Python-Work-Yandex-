code = input()
opened = []
blocks = {}
for i in range(len(code)):
    if code[i] == '[':
        opened.append(i)
    elif code[i] == ']':
        blocks[i] = opened[-1]
        blocks[opened.pop()] = i


x = i = 0
bf = {0: 0}
l = len(code)
while i < l:
    sym = code[i]
    bf.setdefault(x, 0)
    if sym == '>':
        if x == 30000:
            x = 0
        else:
            x += 1
    elif sym == '<':
        if x == 0:
            x = 30000
        else:
            x -= 1
    elif sym == '+':
        if bf[x] == 255:
            bf[x] = 0
        else:
            bf[x] += 1
    elif sym == '-':
        if bf[x] == 0:
            bf[x] = 255
        else:
            bf[x] -= 1
    elif sym == '.':
        print(bf[x])
    elif sym == '[':
        if not bf[x]: i = blocks[i]
    elif sym == ']':
        if bf[x]: i = blocks[i]
    i += 1
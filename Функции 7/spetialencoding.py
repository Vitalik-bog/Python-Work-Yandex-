line, pos = input(), int(input())
pos = len(line)//pos
parts = []
while len(line) > 0:
    if len(line[:pos].strip()) != 0: parts.append(list(line[:pos]))
    line = line[pos:]
parts = list(zip(*parts))
[print(*part, sep='', end='') for part in parts]
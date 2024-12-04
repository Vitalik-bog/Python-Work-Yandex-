n = int(input())
strings = []
for i in range(n):
    strings.append(input())
letter = int(input()) - 1
for j in range(len(strings)):
    if letter < len(strings[j]):
        print(strings[j][letter], end='')
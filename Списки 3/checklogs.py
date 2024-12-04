n = int(input())
words = []
for i in range(n):
    word = input()
    if '####' in word[:4]:
        continue
    if '%%' in word[:2]:
        word = word[2:]
    words += [word]
for i in words:
    print(i)
letters = 'ABCDEFGHI'
n = int(input())
for i in range(n, 0, -1):
    for j in range(n):
        print(letters[j], i, sep='', end=' ')
    print()
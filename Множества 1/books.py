(m, n) = input().split()
library, need = [input() for _ in range(int(m))], [input() for _ in range(int(n))]

for book in need:
    if book in library: print('YES')
    else: print('NO')
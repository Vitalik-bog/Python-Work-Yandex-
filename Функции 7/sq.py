import sys
matrix = [[int(number) for number in line.split()] for line in sys.stdin]
sums = [sum(row) for row in matrix] + [sum(row) for row in list(zip(*matrix))]
if bool(sums) and sums.count(sums[0]) == len(sums): print('YES')
else: print('NO')

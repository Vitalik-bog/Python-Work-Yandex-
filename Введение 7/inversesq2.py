import math
n = int(input())
ressum = 0
for i in range(1, n+1):
    inverse_sq = 1/i**2
    ressum += inverse_sq
print(math.pi**2/ressum)
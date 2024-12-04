n = int(input())
for i in range(1, n+1):
    for x in range(1, n+1):
        print(i*x, end='\t')
    print()
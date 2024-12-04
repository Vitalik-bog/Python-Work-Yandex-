count = int(input())
numbers = []
results = []
for i in range(count):
    numbers += [int(input())]
for i in numbers:
    for j in numbers:
        if not i-j in results:
            results += [i-j]
results.sort()
for res in results:
    print(res)
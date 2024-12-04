peoples = [input() for i in range(int(input()))]
k, repeat = int(input()), int(input())
for i in range(repeat):
    del peoples[k-1::k]
print('\n'.join(peoples))
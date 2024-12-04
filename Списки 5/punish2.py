peoples = [input() for i in range(int(input()))]
k = int(input())
out = []
while len(peoples) > 0:
    out += peoples[::k]
    del peoples[::k]
print('\n'.join(out))
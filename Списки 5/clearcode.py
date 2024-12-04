n = int([i for i in input().split('#')].pop())
out = []
for i in range(n):
    line = input().rstrip()
    if '#' in line:
        line = line[:line.find('#')]
    out += [line.rstrip()]
for e in out:
    print(e)
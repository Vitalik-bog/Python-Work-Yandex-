import itertools
string, (a, b) = input(), [int(i) for i in input().split()]
l, out, string = len(string), [], itertools.cycle(string)
while len(out) < l: out += [next(string).upper() for i in range(a)] + [next(string).lower() for i in range(b)]
print(''.join(out[:l]))

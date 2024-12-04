# -*- coding: utf-8 -*-
import itertools
nominals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
types = ['бубен', 'пик', 'треф', 'червей']
carts, out = itertools.product(nominals, types), []
params = itertools.combinations(carts, 3)
params = filter(lambda param: any(map(lambda card: len(card[0]) > 2, param)), params)
params = filter(lambda param: any(map(lambda card: card[1] == 'червей', param)), params)
params = [sorted([' '.join(p) for p in list(param)]) for param in params]
[out.append(', '.join(param)) for param in params]
print(*sorted(out), sep = '\n')
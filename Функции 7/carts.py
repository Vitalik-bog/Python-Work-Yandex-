# -*- coding: utf-8 -*-
import itertools
carts = [str(i) for i in range(2, 11)]+['валет', 'дама', 'король', 'туз']
types = ('пик', 'треф', 'бубен', 'червей')
data = input()
types = list(filter(lambda x: x != data, types))
print(*[' '.join(cart) for cart in itertools.product(carts, types)], sep='\n')

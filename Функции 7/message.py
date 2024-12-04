# -*- coding: utf-8 -*-
import itertools
dictionary, message, result = [data.lower() for data in input().split()], iter([data.lower() for data in input().split()]), []
for word in message:
   if len(word) >= 7: result.append(word); continue
   arr = [''.join(combination) for combination in list(itertools.permutations(str(word), len(word)))]
   if sum([dictionary.count(combination) for combination in arr if combination != word]) >= 1: result.append('#'*len(word))
   else: result.append(word)
print(' '.join(result))
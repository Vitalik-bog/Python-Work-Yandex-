import pymorphy2
from sys import stdin
words = {}
morph = pymorphy2.MorphAnalyzer()
for line in stdin:
    line = line.rstrip()
    if line == "\x04": break    
    for symbol in line:
        if not symbol.isalnum(): line = line.replace(symbol, ' ')
    line = line.split()
    for part in line:
        word = morph.parse(part)
        if word[0].tag.POS == 'NOUN' and word[0][3] > 0.5:
            name = word[0][2]
            words[name] = words.get(name, 0) + 1
words = list(words.items())
words = list(sorted(words, key = lambda word: word[0], reverse = True))
words = list(sorted(words, key = lambda word: word[1], reverse = True))
[print(word[0], end=' ') for word in words[:10]]
import pymorphy2, sys
morph = pymorphy2.MorphAnalyzer()
words, count = ['видеть', 'увидеть', 'глядеть', 'примечать', 'узреть'], 0
for line in sys.stdin:
    line = line.replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('!', ' ').replace(';', ' ').replace('(', ' ').replace(')', ' ').replace('-', ' ').split()
    for word in line:
        if morph.parse(word)[0][2] in words: count += 1
print(count)
dictwords, words = {}, []
for i in range(int(input())): words += [word.lower() for word in input().split()]
for word in words: dictwords[word] = words.count(word)
words.clear()
for pair in dictwords.items(): words.append([pair[0], pair[1]])
words.sort()
words = [z for z in sorted(words, key=lambda x: -int(x[1]))]   

[print(w[0].title()) for w in words]
line, words = input().split(), {}
[words.update({word:0}) for word in line]
[words.update({word:words[word]+1})==print(words[word], end=' ') for word in line]
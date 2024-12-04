word = list(input().lower())
print(max([word.count(i) for i in word]))
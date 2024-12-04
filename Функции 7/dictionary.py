words = input().split()
print(*sorted(words, key = lambda s: len(s)+ord(s[0].lower())))
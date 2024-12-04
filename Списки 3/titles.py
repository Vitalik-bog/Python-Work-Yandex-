maxlen = int(input())
count = int(input())
titles = []
for i in range(count):
    title = input()
    if len(title) > maxlen:
        title = title[:maxlen-3] + '...'
    titles += [title]
for i in titles:
    print(i)
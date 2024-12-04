count_valid = int(input())
valid = []
out = []
query = ''
for i in range(count_valid):
    valid += [input()]
count_query = int(input())
for i in range(count_query):
    query = input()
    if query in valid:
        out += [query]
for i in range(len(out)):
    print(out[i])
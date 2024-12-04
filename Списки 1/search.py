n = int(input())
strings = []
for i in range(n):
    strings.append(input())
search_line = input()
for j in range(len(strings)):
    if search_line in strings[j]:
        print(strings[j])
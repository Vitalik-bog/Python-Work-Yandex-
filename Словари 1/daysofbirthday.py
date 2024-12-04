calendar, results = {}, []
for i in range(int(input())):
    data = input().split()
    if data[2] in calendar: calendar.update({data[2]:calendar[data[2]]+[data[0]]})
    else: calendar.update({data[2]:[data[0]]})
for i in range(int(input())):
    word = input()
    if word in calendar: results.append(' '.join(sorted(calendar[word])))
    else: results.append('')
[print(i) for i in results]
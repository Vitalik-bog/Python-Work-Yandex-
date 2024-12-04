def sorting(data):
    array = [[(d) for d in row.split()] for row in data]
    array.sort()
    array = [' '.join(z) for z in sorted(array, key=lambda x: int(x[1]))]
    return array

calendar, results = {}, []
for i in range(int(input())):
    data = input().split()
    if data[2] in calendar: calendar.update({data[2]:calendar[data[2]]+[data[0]+' '+data[1]]})
    else: calendar.update({data[2]:[data[0]+' '+data[1]]})
for i in range(int(input())):
    word = input()
    if word in calendar: results.append(' '.join(sorting(calendar[word])))
    else: results.append('')
[print(i) for i in results]
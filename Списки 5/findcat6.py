data = [input() for i in range(int(input()))]
for d in range(len(data)):
    if 'кот' in data[d]:
        print(d+1, data[d].find('кот')+1)

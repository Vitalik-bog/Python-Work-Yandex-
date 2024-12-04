peoples, peoples_array = {}, []
for i in range(int(input())):
    data = input()
    peoples[data] = peoples.get(data, 0)+1
for name, count in peoples.items():
    peoples_array.append([name, count])
peoples_array.sort()
peoples_array = [z for z in sorted(peoples_array, key=lambda x: -int(x[1]))]
[print(pair[0], pair[1]) for pair in peoples_array]
books = [i for i in input().split('\t') if len(i) > 0]
data = list(zip(input().split('\t'), input().split('\t'), input().split('\t')))
shops = data.pop(data.index(data[0]))
data, temp = [sum([int(n) for n in [i[l] for i in list(data)]]) for l in range(len(data))], data[:]
res_index = data.index(min(data))
print(shops[res_index])
data = [int(n) for n in [i[res_index] for i in list(temp)]]
[print(books[i].strip()+'\t'+str(data[i])) for i in range(len(data))]
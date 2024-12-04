dictionary = {}
for i in range(int(input())): 
    data = input().split()
    dictionary.update({data[0]:' '.join(data[1:])})
for i in range(int(input())):
    word = input()
    if word in dictionary: print(dictionary[word])
    else: print('Нет в словаре')
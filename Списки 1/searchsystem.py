count_data = int(input())
data = []
for i in range(count_data):
    data += [input()]
count_query = int(input())
query = []
for i in range(count_query):
    query += [input()]
out = []
isset = False
for i in range(len(data)):
    for j in range(len(query)):
        if query[j] in data[i]:
            isset = True
        else: 
            isset = False
            break
    if isset == True: 
        print(data[i])
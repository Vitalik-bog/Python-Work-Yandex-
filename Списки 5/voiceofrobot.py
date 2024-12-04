data = [i+'-' for i in input().upper()]
data = ''.join(data)
data = data.replace('- -', ' ')
print(data[:-1])
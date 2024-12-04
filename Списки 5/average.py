data = [float(i) for i in input().split()]
data.sort()
average = sum(data)/len(data)
if len(data) % 2 != 0:
    median = float(data[len(data) // 2])
else:
    median = float((data[len(data) // 2 -1] + data[len(data) // 2])/2)
print(round(average, 3), round(median, 3))

count = int(input())
data = []
abv = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзиклмнопрстуфхцчшщъыьэюя'
for i in range(count):
	data += [input()]
data.sort()
for i in data:
	print(i)
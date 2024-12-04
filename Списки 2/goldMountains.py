clients = int(input())
money = []
for i in range(clients):
	money += [int(input())]
for i in money:
	print(i)
print()
for i in money:
	print(i*3)
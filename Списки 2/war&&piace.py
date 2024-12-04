n = int(input())
war = 'Евразия'
piace = 'Остазия'
comands = []
for i in range(n):
	comands += [input()]
for comand in comands:
	if comand == 'С кем война?':
		print(war)
	elif comand == 'С кем мир?':
		print(piace)
	elif comand == 'Меняем':
		war, piace = piace, war
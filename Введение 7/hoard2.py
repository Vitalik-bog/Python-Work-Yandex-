hoard = [int(input()), int(input())]
user = [0, 0]
i = 0
steps_final = 0
side_final = ''
default = 'север'
if user != hoard:	
	side = input()
	while side != 'стоп':
		if side == 'вперёд':
			steps = int(input())
			if default == 'север':
				user[1] += steps
			elif default == 'юг':
				user[1] -= steps
			elif default == 'восток':
				user[0] += steps
			elif default == 'запад':
				user[0] -= steps
		elif side == 'налево':
			if default == 'север':
				default = 'запад'
			elif default == 'юг':
				default = 'восток'
			elif default == 'восток':
				default = 'север'
			elif default == 'запад':
				default = 'юг'
		elif side == 'направо':
			if default == 'север':
				default = 'восток'
			elif default == 'юг':
				default = 'запад'
			elif default == 'восток':
				default = 'юг'
			elif default == 'запад':
				default = 'север'
		elif side == 'разворот':
			if default == 'север':
				default = 'юг'
			elif default == 'юг':
				default = 'север'
			elif default == 'восток':
				default = 'запад'
			elif default == 'запад':
				default = 'восток'
		i += 1
		if user == hoard and steps_final == 0:
			steps_final = i
			side_final = default
			print(steps_final)
			print(side_final)
			break
		side = input()
	if user != hoard and steps_final == 0:
		print(steps_final)
		print(default)
else:
	print(steps_final)
	print(default)
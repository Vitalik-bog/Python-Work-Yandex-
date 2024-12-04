city_1 = input()
city_2 = input()
error = 'НЕТ'
success = 'ДА'
if city_1 == 'Тула' or city_2 == 'Пенза':
  if city_1 == city_2:
    print(error)
  elif city_1 == 'Тула' and city_2 == 'Пенза':
    print(error)
  else:
    print(success)
else:
  print(error)
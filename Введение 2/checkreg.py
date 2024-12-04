login = input()
address = input()


if '@' in address and not '@' in login:
   print('OK') 
else:
   if '@' in login:
      print('Некорректный логин')
   elif not '@' in address:
      print('Некорректный адрес')
    
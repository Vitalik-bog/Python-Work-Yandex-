password_1 = input()
password_2 = input()

if len(password_1) < 8:
    print('Короткий!')
elif '123' in password_1:
    print('Простой!')
elif password_2 != password_1:
    print('Различаются.')
else:
    print('OK')
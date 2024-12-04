password_1 = input()
password_2 = input()

while len(password_1) < 8 or '123' in password_1 or password_2 != password_1:
    if len(password_1) < 8:
        print('Короткий!')
    elif '123' in password_1:
        print('Простой!')
    elif password_2 != password_1:
        print('Различаются.')
    password_1 = input()
    password_2 = input()  
       
print('OK')
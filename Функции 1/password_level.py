def password_level(password):
    if len(password) >= 6:
        if not(password.isdigit() or password == password.lower() or password == password.upper()):
            if not(password.isalpha() or password == password.lower() or password == password.upper()):
                print('Надежный пароль')
            else:
                print('Слабый пароль')
        else:
            print('Ненадежный пароль')
    else:
        print('Недопустимый пароль')
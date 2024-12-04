pass_1 = input()
pass_2 = input()

if len(pass_1) < 8:
    print('Короткий!')
else:
    if pass_1 != pass_2:
        print('Различаются.')
    else:
        print('OK')
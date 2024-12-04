In = input()
data = []
while In != '':
    data += [In.split(':')]
    In = input()
bad = input().split(';')
finded_logins = []
finded_names = []
for user in data:
    for i in range(len(user)):
        for b in bad:
            if user[1] == b and not user[0] in finded_logins:
                finded_logins += [user[0]]
                finded_names += [user[4].split(',')[0]]
for object in range(len(finded_logins)):
    print('To:', finded_logins[object])
    print(finded_names[object]+',', 'ваш пароль слишком простой, смените его.')
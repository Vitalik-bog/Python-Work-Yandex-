city_1 = input()
city_2 = input()
if city_1[-1] == 'ь':
    if city_1[-2] == city_2[0]:
        print('ВЕРНО')
    else:
        print('НЕВЕРНО')
else:
    if city_1[-1] == city_2[0]:
        print('ВЕРНО')
    else:
        print('НЕВЕРНО')
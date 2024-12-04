b = 99
words = ['бутылка', 'бутылки', 'бутылок']
while b != -1:
    if (str(b)[-1] == '4' and b != 14) or (str(b)[-1] == '3' and b != 13) or (str(b)[-1] == '2' and b != 12):
        word = words[1]
    elif str(b)[-1] == '1' and b != 11:
        word = words[0]
    else:
        word = words[2]
    if b == 0:
        break
    print('В холодильнике', b, word, 'кваса. ')
    print('Возьмём одну и выпьем. ')
    b -= 1
    if (str(b)[-1] == '4' and b != 14) or (str(b)[-1] == '3' and b != 13) or (str(b)[-1] == '2' and b != 12):
        word = words[1]
    elif str(b)[-1] == '1' and b != 11:
        word = words[0]
    else:
        word = words[2]
    print('Осталось', b, word, 'кваса. ')

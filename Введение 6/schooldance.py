wait = int(input())
word = ''
correct = ['раз', 'два', 'три', 'четыре']
corint = 0
i = 0
while wait != 0:
    word = input()
    if word != correct[i]:
        print('Правильных отсчётов было ', corint, ', но теперь вы ошиблись.', sep='')
        i = 0
        corint = 0
        wait -= 1
    else:
        corint += 1
        i += 1
        if i == 4:
            i = 0
print('На сегодня хватит.')
message = input()
index = int(input()) - 1
letter = input()

if index >= 0 and index < len(message) and len(letter) == 1:
    if message[index] == letter:
        print('ДА')
    elif message[index] != letter:
        print('НЕТ')
else:
    print('ОШИБКА')
message = input()
letter = int(input())
if letter <= 0 or letter > len(message) :
    print('ОШИБКА')
else:
    print(message[letter - 1])
valid = 'qwertyuiopasdfghjklzxcvbnm1234567890_'
word = input()
success = True
for i in range(len(word)):
    if not word[i] in valid:
        success = False
        print('Неверный символ:', word[i])
        break   
if success:
    print('OK')
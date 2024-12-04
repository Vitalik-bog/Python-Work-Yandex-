word = input()
word_max = ""
word_min = ""
result = False
i=0
word_min = word
while word != "стоп":
    if len(word) > len(word_max):
        word_max = word
    if len(word) < len(word_min):
        word_min = word
    word = input()    
while i < len(word_min):
    if word_min[i] in word_max:
        result = True
    else:
        result = False
        break
    i+=1
if result == True:
    print('ДА')
else:
    print('НЕТ')
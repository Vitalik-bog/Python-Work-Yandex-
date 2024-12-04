word_1 = input()
word_2 = input()
bulls = 0
cows = 0
for i in range(len(word_1)):
    if word_1[i] == word_2[i]:
        bulls+=1
    elif word_1[i] in word_2:
        cows+=1
print(bulls, cows)
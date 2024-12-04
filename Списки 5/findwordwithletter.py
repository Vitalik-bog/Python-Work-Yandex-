letter = input()
data = [i for i in input().split()]
for i in data:
    if letter.lower() in i or letter.upper() in i:
        print(i)
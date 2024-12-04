s = int(input())
progress_1 = []
for i in range(s):
    progress_1 += [int(input())]
    
progress_2 = progress_1[:]

count = int(input())
for i in range(count):
    if int(input()) == 1:
        p = int(input())
        progress_1[p] += int(input())
    else:
        p = int(input())
        progress_2[p] += int(input())
count = 0
for i in progress_1:
    print(i, end = ' ')
print()
for i in progress_2:
    print(i, end = ' ')
    
for i in range(len(progress_1)):
    if progress_1[i] == progress_2[i]:
        count += 1
print()
print(count)

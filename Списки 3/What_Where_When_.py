import math
count = int(input())
comands = []
scores = []
for i in range(count):
    comands += [input()]
    scores += [int(input())]
final_count = math.ceil(count/2)
final_comands = comands[:]
for i in range(count - final_count):
    m = min(scores)
    for j in range(len(scores)):
        if scores[j] == m:
            del scores[j]
            break
    del final_comands[j]
final_comands.sort()
for f in final_comands:
    print(f)
comands.sort()
for c in comands:
    if not c in final_comands:
        print(c)
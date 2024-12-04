import sys
programm, count = input(), 0
for line in sys.stdin:
    if '#' in line: count+= 1
print(count)
count = int(input())
students = []
for i in range(count):
    students += [input()]
for i in students:
    print(i)
print()
for i in students:
    if i[-1] in ['4', '5']:
        print(i)
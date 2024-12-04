n = int(input())
thimbles = []
elements = []
for i in range(n):
    thimbles += [input()]
k = int(input())
for i in range(k):
    n = int(input())
    for j in range(n):
        elements += [thimbles[int(input())-1]]
    thimbles = elements
    elements = []
for i in range(len(thimbles)):
    print(thimbles[i])
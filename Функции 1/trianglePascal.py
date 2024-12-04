import re
def current_row(num):
    i = 0
    a = []
    while i < num:
        if i == 0:
            a.append([1])
        elif i == 1:
            a.append([1,1])
        else:
            at = [1]
            for j in range(len(a[i-1])-1):
                at.append(a[i-1][j]+a[i-1][j+1])
            at.append(1)
            a.append(at)
        i += 1
    return a[-1]

      
def printPascalTriangle():
    m = int(input())
    for i in range(m):
        arr = [str(i) + '\t\t' for i in current_row(i+1)]
        edit(m, i, arr)
        arr[-1] = arr[-1][:-2]
        p(arr)
        
def edit(m, i, arr):
    while len(arr) < m*2-i-1:
        arr.insert(0, '\t')
        arr.append('\t')
        
def p(arr):
    string = ''.join(arr)
    res = re.match('\t', string)
    if res:
        string = string[:-res.end()]
    print(string)    
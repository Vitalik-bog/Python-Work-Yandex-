def printMultiplicationTable(n, k):
    for i in range(1, n+1):
        string = ''
        for j in range(1, k+1):
            string += str(i*j)+ '\t'
        print(string[:-1])
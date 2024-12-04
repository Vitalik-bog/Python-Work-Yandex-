def printMultiplicationTable():
    for i in range(1, 10):
        string = ''
        for j in range(1, 10):
            string += str(i*j)+ '\t'
        print(string[:-1])
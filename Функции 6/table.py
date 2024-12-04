def printOperationTable(operation, numRows=9, numColumns=9):
    for i in range(1, numRows+1):
        for j in range(1, numColumns+1):
            print(operation(i, j), end='   ')
        print()

def goldenRatio(i):
    fibb = [1, 1]
    if i == 0:
        i = 1
    for j in range(0, i+1):
        fibb += [fibb[-1]+fibb[-2]]

    print(fibb[j]/fibb[j-1])

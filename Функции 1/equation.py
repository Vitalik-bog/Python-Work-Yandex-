def equation(data_1, data_2):
    data_1 = [float(i) for i in data_1.split(';')]
    data_2 = [float(i) for i in data_2.split(';')]
    x1, y1 = data_1[0], data_1[1]
    x2, y2 = data_2[0], data_2[1]
    if y1-y2 == 0 and (x1 - x2) != 0 or x1-x2 == 0 and y1-y2 != 0:
        k = 0
    else:
        k = (y1 - y2) / (x1 - x2)
    b = y2 - k*x2
    if (k == y1 or k == y2) or (b == y1 or b == y2 and y1==y2):
        if k == y1 or k == y2:
            print(k)
        if b == y1 or b == y2 and y1==y2:
            print(b)
    else:
        print(k, b)
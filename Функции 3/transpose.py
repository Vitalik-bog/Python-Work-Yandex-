def transpose(matrix):
    array, temp_array = [], []
    if bool(matrix):
        for i in range(len(matrix[0])):
            for element in matrix: temp_array.append(element[i])
            array += [temp_array]
            temp_array = []
        matrix.clear()
        matrix = [matrix.append(i) for i in array]


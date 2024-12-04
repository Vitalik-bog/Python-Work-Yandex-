def findMountain(heightsMap):
    result = [0,0,0]
    for column in heightsMap:
        height = max(column)
        if height > result[2]: result = [heightsMap.index(column), column.index(height), height]
    return result[0], result[1]
def possibleTurns(cell):
    cell, desk, results = transform(cell), 8*[8*[[]]], []
    n, m = 1, 2
    for i in range(9):
        if check((cell[0]-n, cell[1]+m), results): results += [transform((cell[0]-n, cell[1]+m), back=True)]
        if check((cell[0]+n, cell[1]+m), results): results += [transform((cell[0]+n, cell[1]+m), back=True)]
        if check((cell[0]-n, cell[1]-m), results): results += [transform((cell[0]-n, cell[1]-m), back=True)]
        if check((cell[0]+n, cell[1]-m), results): results += [transform((cell[0]+n, cell[1]-m), back=True)]
        if i == 7: n, m = 2, 1
    return results
    
def transform(data, back=False):
    coords = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    if not back: return coords.index(list(data)[0])+1, int(list(data)[1])
    return coords[data[0]-1] + str(data[1])
def check(coords, repeatarr):
    if (coords[0] > 0 and coords[0] <= 8) and (coords[1] > 0 and coords[1] <= 8) and not transform(coords, back=True) in repeatarr: return True
    return False
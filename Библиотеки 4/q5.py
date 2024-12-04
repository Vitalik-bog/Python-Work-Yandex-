
Queens = []

def generate(current_column, count, variant):
    if len(variant) == count: Queens.append(''.join(map(lambda x: str(x+1), variant)))
    else:
        for queen in range(count):
            if isvalid((queen, current_column), variant): generate(current_column+1, count, variant+[queen])

def isvalid(coords, variant):
    x, y = coords
    for j in range(len(variant)):
        if (variant[j] == x or abs(j - y) == abs(variant[j] - x)):
                return False
    return True
size = int(input())
for n in range(size):
    generate(1, size, [n])
print(*Queens, sep='\n')
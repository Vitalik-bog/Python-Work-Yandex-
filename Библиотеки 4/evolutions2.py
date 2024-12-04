def generate(data):
    old = data.copy()
    new = [1 for i in range(len(old))]
    for num in range(len(new)):
        if num+1 < len(new): neighbors = [old[num-1], old[num], old[num+1]]
        else: neighbors = [old[num-1], old[num], old[0]]
        if neighbors.count(neighbors[0]) == len(neighbors) or neighbors[0]+neighbors[1] == 2 or neighbors[0] + neighbors[2] == 2: new[num] = 0
    return new    

evolute = [int(_) for _ in input()]
for i in range(10):
    evolute = generate(evolute)
print(''.join([str(i) for i in evolute]))
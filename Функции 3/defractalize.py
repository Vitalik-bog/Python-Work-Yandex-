def defractalize(fractal):
    d = []
    for branch in range(len(fractal)):
        if fractal[branch] == fractal: d += [fractal[branch]]
    for element in d:
        del fractal[fractal.index(element)]
    
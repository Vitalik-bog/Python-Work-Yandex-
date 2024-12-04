def fractal_print(fractal):
    data = fractal[:]
    for branch in range(len(fractal)):
        if fractal[branch] == fractal:
            fractal[branch] = data
    print(fractal)

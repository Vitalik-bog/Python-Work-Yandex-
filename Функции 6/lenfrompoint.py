# -*- coding: utf-8 -*-
def astroid(R, t, point):
    import math
    x = R * math.cos(t)**3
    y = R * math.sin(t)**3
    return math.sqrt((x-point[0])**2 + (y-point[1]**2))
print(astroid(1, 1, (0.75, 0)))
print(astroid(0, 1, (0.75, 0))) #Самое маленькое расстояние при R == 0 => 0.75
print(astroid(0.25, 1, (0.75, 0)))
print(astroid(1, 1, (0.75, 0)))
print(astroid(1, 1, (0.75, 0)))
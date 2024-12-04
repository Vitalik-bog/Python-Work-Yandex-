import math
def roots_of_quadratic_equation(a,b,c):
    if a == 0 and b == 0 and c != 0: return []
    if b == 0 and c == 0: return ['all']
    if b == 0 and c != 0:
        x_2 = -c/a
        if x_2 > 0: return [math.sqrt(x_2), -math.sqrt(x_2)]
        elif x_2 == 0: return ['all']
        return []
    if a == 0 and b != 0: return [-c/b]
    if c == 0 and a != 0: return [0, -b/a]
    d = (b**2)-4*a*c
    #print(d)
    if d > 0: return [(-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a)]
    elif d == 0: return [-b/2*a]
    else: return []
#print(roots_of_quadratic_equation(0,0,1))

import math

def discriminant(a,b,c):
    return (b**2)-4*a*c

def larger_root(p,q):
    res, d = [], discriminant(1, p, q)
    x1, x2 = (-p + math.sqrt(d))/2, (-p - math.sqrt(d))/2,
    if x1 > x2: return x1
    else: return x2
    
def smaller_root(p,q):
    res, d = [], discriminant(1, p, q)
    x1, x2 = (-p + math.sqrt(d))/2, (-p - math.sqrt(d))/2,
    if x1 < x2: return x1
    else: return x2
    
def main():
    p, q = float(input()), float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p,q), larger_root(p,q))

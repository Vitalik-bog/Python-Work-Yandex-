def main():
    radius = float(input())
    print(circleLength(radius), circleArea(radius))

def circleLength(radius):
    return 2*3.14159*radius

def circleArea(radius):
    return radius**2*3.14159


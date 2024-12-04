import math
def findFarthestOrbit(listOfOrbits):
    squares = [coords[0]*math.pi*coords[1] for coords in listOfOrbits if coords[0] != coords[1]]
    return [coords for coords in listOfOrbits if coords[0]*coords[1]*math.pi == max(squares)][0]

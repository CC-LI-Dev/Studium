import math
def distance(x1: float, y1: float, x2: float, y2: float, z: float) -> float:
    dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2)) + 2*z
    return dist

print(distance(1.0,1.0,0.0,2.0,10.0))
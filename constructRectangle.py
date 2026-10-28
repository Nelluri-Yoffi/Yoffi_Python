import math

def constructRectangle(area: int) -> list[int]:
    w = math.isqrt(area)
    while area % w != 0:
        w -= 1
    return [area // w, w]
print(constructRectangle(4))     

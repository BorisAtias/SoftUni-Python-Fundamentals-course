import math
from math import floor

def get_distance(_x1, _y1, _x2, _y2):
    return math.sqrt(math.pow(_x2 - _x1, 2.0) + math.pow(_y1 - _y2, 2.0))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

dist1 = get_distance(x1, y1, 0, 0)
dist2 = get_distance(x2, y2, 0, 0)

if dist1 <= dist2:
    print((f'({floor(x1)}, {floor(y1)})'))
else:
    print(f'({floor(x2)}, {floor(y2)})')
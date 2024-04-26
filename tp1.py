import math

def calc_distance(point1, point2):
    distance_squared = sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2))
    return math.sqrt(distance_squared)

def my_map(func, *iterables):
    return [func(*args) for args in zip(*iterables)]

points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

distances = my_map(calc_distance, points1, points2)

print(distances)

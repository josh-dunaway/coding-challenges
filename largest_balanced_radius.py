'''
Prompt:
Given a set of points on a plane, find the largest number of points 
that can be enclosed within a circle centered on the origin, such 
that the number of red points and green points inside it is equal.

My plan:
Map the given coordinates based on the index of x, y coordinate
    key = index
    value = [x_coord, y, coord, distance, color]

I then create a list of keys (indexes) sorted by distance from origin

Finally, I iterate through keys (radiate outwards from origin)
and keep tally of green and red points.
If greens == reds, I update max_equal points = greens + reds

For some reason, my code is only 33% correct according to Codility..
they don't give specific input data where I failed, so I'm not 
sure what to fix at the moment
'''

def solution(X, Y, colors):

    greens = 0
    reds = 0
    max_equal_points = 0

    coordinate_map = _getDictOfPointsWithDistanceFromOrigin(X, Y, colors)
    keys_sorted_by_distance = _keysSortedByDistanceFromOrigin(coordinate_map)

    for key in keys_sorted_by_distance:
        if coordinate_map.get(key)[3].lower() == 'g':
            greens += 1
        else:
            reds += 1
        if greens == reds:
            max_equal_points = greens + reds

    return max_equal_points

# key will be index, values will be coords, colors, and distance from origin


def _getDictOfPointsWithDistanceFromOrigin(x_coords: list, y_coords: list, colors: str) -> dict:
    import math
    coordinate_map = {}
    for i in range(len(x_coords)):
        coordinate_map[i] = [x_coords[i], y_coords[i], math.sqrt(
            (x_coords[i]**2) + (y_coords[i]**2)), colors[i]]
    return coordinate_map


def _keysSortedByDistanceFromOrigin(coordinate_map: dict) -> list:
    return sorted(coordinate_map.keys(), key=lambda x: coordinate_map[x][2])


def main():
    wire1 = []
    wire2 = []

    with open("input", 'r') as fp:
        wire1 = parse_coordinates(fp.readline())
        wire2 = parse_coordinates(fp.readline())
    
    # Loop through all the line segments in wire1 and wire2 to see where they intersect
    intersections = []
    for i in range(len(wire1) - 1):
        for j in range(len(wire2) - 1):
            p1 = wire1[i]
            q1 = wire1[i + 1]
            p2 = wire2[j]
            q2 = wire2[j + 1]
            if (lines_intersect(p1, q1, p2, q2)):
                intersections.append(calculate_intersection(p1, q1, p2, q2))

    print("The two wires intersect at the following points:")
    print (intersections)

    min_dist = 0
    for point in intersections:
        dist = calculate_wire_distance(point, wire1) + calculate_wire_distance(point, wire2)
        if (min_dist == 0):
            min_dist = dist
        elif (min_dist > dist):
            min_dist = dist
    
    print("Closest intersection is at distance of {}.".format(min_dist))


def parse_coordinates(line):
    paths = line.split(',')
    x = y = 0
    coordinates = [(x, y)]
    for path in paths:
        direction = path[0:1]
        distance = int(path[1:])

        if direction == 'D':
            y -= distance
        elif direction == 'U':
            y += distance
        elif direction == 'L':
            x -= distance
        elif direction == 'R':
            x += distance
        
        coordinates.append((x, y))
    
    return coordinates


def lines_intersect(p1, q1, p2, q2):
    '''
    Checks if the two line segments given by (p1, q1) and (p2, q2) intersects.
    Adapted from https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
    '''
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    intersect = False

    # general case
    if (o1 != o2 and o3 != o4):
        intersect = True
    
    # Ignore colinear cases for purposes of this puzzle
    return intersect


def orientation(p, q, r):
    ''' Checks orientation of ordered triplet (p, q, r).
        Returns:
            0 --> points are colinear
            1 --> clockwise
            2 --> counter-clockwise
    '''
    value = (q[1] - p[1]) * (r[0] - q[0])
    value -= (q[0] - p[0]) * (r[1] - q[1])

    if (value == 0):
        return 0
    elif (value >0):
        return 1
    else:
        return 2


def calculate_intersection(p1, q1, p2, q2):
    ''' Calculates the intersection point of line segments (p1, q1) and (p2, q2).
        Adapted from https://stackoverflow.com/a/1968345
    '''
    s1_x = q1[0] - p1[0]
    s1_y = q1[1] - p1[1]
    s2_x = q2[0] - p2[0]
    s2_y = q2[1] - p2[1]

    s = (-s1_y * (p1[0] - p2[0]) + s1_x * (p1[1] - p2[1])) / (-s2_x * s1_y + s1_x * s2_y)
    t = ( s2_x * (p1[1] - p2[1]) - s2_y * (p1[0] - p2[0])) / (-s2_x * s1_y + s1_x * s2_y)

    (x, y) = (0, 0)
    if (s >= 0 and s <= 1 and t >= 0 and t <= 1):
        # Collision detected
        x = int(p1[0] + (t * s1_x))
        y = int(p1[1] + (t * s1_y))
    
    return (x, y)


def calculate_wire_distance(p, wire):
    ''' Calculates the number of steps needed to get to given point (p) for given wire '''

    distance = 0
    for i in range(len(wire) - 1):
        # Check if point p lies on current length of wire
        if (point_on_segment(p, wire[i], wire[i + 1])):
            distance += int(abs(wire[i][0] - p[0]) + abs(wire[i][1] - p[1]))
            return distance
        else:
            distance += int(abs(wire[i][0] - wire[i + 1][0]) + abs(wire[i][1] - wire[i + 1][1]))
    
    return distance


def point_on_segment(x, p, r):
    ''' Checks if point x lies on line segment 'pr'.'''

    if (x[0] != p[0] and x[1] != p[1]):
        # point x shares neither x nor y coordinates, hence it isn't on the current segment
        return False
    
    if (x[0] <= max(p[0], r[0])
        and x[0] >= min(p[0], r[0])
        and x[1] <= max(p[1], r[1])
        and x[1] >= min(p[1], r[1])
        ):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
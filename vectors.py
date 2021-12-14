from math import *


def distance(point_a, point_b):
    return sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)


def angle_between_points(point_a, point_b):
    r = distance(point_a, point_b)  # length of hypotenuse
    x = abs(point_b[0] - point_a[0])  # length of opposite
    if r == 0:
        return 0
    angle = round(degrees(asin(x / r)))

    if point_b[0] - point_a[0] > 0 and point_b[1] - point_a[1] > 0:
        # first quarter
        return angle
    elif point_b[0] - point_a[0] > 0 and point_b[1] - point_a[1] < 0:
        # second quarter
        return 180 - angle
    elif point_b[0] - point_a[0] <= 0 and point_b[1] - point_a[1] < 0:
        # third quarter
        return 180 + angle
    elif point_b[0] - point_a[0] < 0 and point_b[1] - point_a[1] >= 0:
        # fourth quarter
        return 360 - angle
    return angle


def coordinates(point, radius, angle):
    x = point[0] + radius * sin(radians(angle))
    y = point[1] + radius * cos(radians(angle))
    return [x, y]


def parameters(point_a, point_b):
    ap = (point_a[1] - point_b[1]) / (point_a[0] - point_b[0])
    bp = point_a[1] - point_a[0] * (point_a[1] - point_b[1]) / (point_a[0] - point_b[0])
    return [ap, bp]


def vector_coordinates(angle, length):
    x = length * sin(radians(angle))
    y = length * cos(radians(angle))
    return x, y


def values_square(value, size):
    return values_2d(value, size, size)


def values_2d(value, size_x, size_y):
    return [[value for i in range(size_y)] for j in range(size_x)]


def get_real_coordinates(i, j, vector):
    x = i + vector[0]
    y = j + vector[1]
    return x, y


def no_go_angles(polar, wind_speed, wind_angle):
    no_go_angle = 0
    for angle in range(360):
        if polar[angle][wind_speed] != 0:
            no_go_angle = angle
            break
    no_go_angle_left = (wind_angle - no_go_angle) % 360
    no_go_angle_right = (wind_angle + no_go_angle) % 360
    return no_go_angle_left, no_go_angle_right


def alter_no_go_angles(no_go_angles, current, drift):
    left_end_coordinates = coordinates((0, 0), 1, no_go_angles[0])
    right_end_coordinates = coordinates((0, 0), 1, no_go_angles[1])

    left_end_resultant = [left_end_coordinates[0] + current[0] + drift[0],
                          left_end_coordinates[1] + current[1] + drift[1]]
    right_end_resultant = [right_end_coordinates[0] + current[0] + drift[0],
                           right_end_coordinates[1] + current[1] + drift[1]]

    left_altered_no_go_angle = angle_between_points((0, 0), left_end_resultant)
    right_altered_no_go_angle = angle_between_points((0, 0), right_end_resultant)

    return left_altered_no_go_angle, right_altered_no_go_angle

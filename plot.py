from algorithm import *
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def grid_density(length):
    if length <= 15:
        return 1
    return round(length / 10)


def end_of_line_coordinates(point, length, angle):
    x = point[0] + length * sin(radians(angle))
    y = point[1] + length * cos(radians(angle))
    return x, y


def create_plot(algorithm_outputs):
    # clear figure
    plt.clf()

    limits = algorithm_outputs.limits
    point_A = algorithm_outputs.point_A
    point_B = algorithm_outputs.point_B
    point_C = algorithm_outputs.point_C
    course_A_B = algorithm_outputs.yacht_course_A_B
    real_speed_A_B = algorithm_outputs.real_speed_A_B
    course_B_C = algorithm_outputs.yacht_course_B_C
    real_speed_B_C = algorithm_outputs.real_speed_B_C

    # courses ends coordinates for plot
    course_A_B_end = end_of_line_coordinates(point_A, real_speed_A_B, course_A_B)
    course_B_C_end = end_of_line_coordinates(point_B, real_speed_B_C, course_B_C)

    # no go zone end coordinates for plot
    length = (limits[1]-limits[0])
    left_no_go_zone_end = end_of_line_coordinates(point_A, length, algorithm_outputs.no_go_angles_A[0])
    right_no_go_zone_end = end_of_line_coordinates(point_A, length, algorithm_outputs.no_go_angles_A[1])

    # route
    plt.plot([point_A[0], point_B[0], point_C[0]], [point_A[1], point_B[1], point_C[1]], 'y--', linewidth=1)
    # points
    plt.plot(point_A[0], point_A[1], 'ro')
    plt.plot(point_B[0], point_B[1], 'bo')
    plt.plot(point_C[0], point_C[1], 'go')
    # points texts
    plt.text(point_A[0], point_A[1], 'A', fontsize=15)
    plt.text(point_B[0], point_B[1], 'B', fontsize=15)
    plt.text(point_C[0], point_C[1], 'C', fontsize=15)
    # courses
    plt.plot([point_A[0], course_A_B_end[0]], [point_A[1], course_A_B_end[1]], 'r--')
    plt.plot([point_B[0], course_B_C_end[0]], [point_B[1], course_B_C_end[1]], 'b--')
    # no_go_zone
    plt.plot([point_A[0], left_no_go_zone_end[0]], [point_A[1], left_no_go_zone_end[1]], 'c-.')
    plt.plot([point_A[0], right_no_go_zone_end[0]], [point_A[1], right_no_go_zone_end[1]], 'c-.')

    plt.axis('square')

    plt.xlim((limits[0], limits[1]))
    plt.ylim((limits[2], limits[3]))

    density = grid_density(limits[1] - limits[0])

    plt.gca().xaxis.set_major_locator(MultipleLocator(density))
    plt.gca().yaxis.set_major_locator(MultipleLocator(density))

    plt.grid(color='b', linestyle='--', linewidth=0.1)

    plot_file_name = 'plot.png'

    plt.savefig(plot_file_name)

    # clear figure
    plt.clf()

    return plot_file_name


def create_indicator(angle, color, file_name):
    # clear figure
    plt.clf()

    circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
    tip = coordinates((0, 0), 1, angle + 180)

    plt.arrow(0, 0, tip[0], tip[1], width=0.1, head_width=0.1, head_length=0.5, length_includes_head=True, color=color)

    plt.axis('off')

    fig = plt.gcf()
    ax = fig.gca()

    ax.add_artist(circle)
    ax.set_xlim((-1.1, 1.1))
    ax.set_ylim((-1.1, 1.1))
    ax.set_aspect('auto')

    fig.savefig(file_name)

    # clear figure
    plt.clf()

    return file_name

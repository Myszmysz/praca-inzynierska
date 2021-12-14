from vectors import *
import time


class InputDataError(Exception):
    pass


def check_input_values(wind_speed, polar_data, point_A, point_C):
    if wind_speed < 1:
        raise InputDataError("no wind, not possible to calculate")
    if wind_speed > len(polar_data[0]):
        raise InputDataError("yacht characteristic in given wind speed not available")
    if point_A == point_C:
        raise InputDataError("target coordinates are same as start")


def algorithm(point_C, algorithm_preconditions):

    # INPUT DATA
    point_A = algorithm_preconditions.point_A
    wind_speed = algorithm_preconditions.wind_speed
    wind_angle = algorithm_preconditions.wind_angle
    current_speed = algorithm_preconditions.current_speed
    current_angle = algorithm_preconditions.current_angle
    polar_data = algorithm_preconditions.polar_data

    # CHECK INPUT DATA VALUES
    check_input_values(wind_speed, polar_data, point_A, point_C)

    drift_efficiency = 0.025  # intensity of wind impact on yacht

    # FORMAT INPUT DATA
    wind_speed = round(wind_speed)
    current_angle = round(current_angle % 360)
    wind_angle = round(wind_angle % 360)

    # INITIAL CALCULATIONS
    current_vector = vector_coordinates(current_angle, current_speed)  # current vector
    drift_vector = vector_coordinates(wind_angle, -drift_efficiency * wind_speed)  # drift vector

    distance_A_C = distance(point_A, point_C)  # distance between A and C points
    search_radius = ceil(distance_A_C)

    # time between point A and B
    time_A_B = 0
    time_B_C = 0
    while_loop_iteration = 0
    max_loop_iteration = 8
    computing_time = time.time()
    max_computing_time = 120  # seconds

    while time_A_B <= 0 or time_B_C <= 0:

        while_loop_iteration += 1
        if while_loop_iteration >= max_loop_iteration or search_radius > 1024:
            raise InputDataError("current too strong: cannot calculate the route")
        print("search radius: ", search_radius, " computing time: ", round(time.time() - computing_time,2)," s")
        if time.time() - computing_time > max_computing_time:
            raise InputDataError("computing time limit exceeded: cannot calculate the route")

        search_diameter = 2 * search_radius + 1  # surroundings of point A
        licit_B_position = values_square(1, search_diameter)  # matrix of possible B point locations
        shift_vector = (point_A[0] - search_radius, point_A[1] - search_radius)  # relocate center of matrix to point A

        # NO-GO ZONE ANGLES CALCULATIONS
        no_go_angles_A = no_go_angles(polar_data, wind_speed, wind_angle)
        no_go_angles_C = ((no_go_angles_A[0] + 180) % 360, (no_go_angles_A[1] + 180) % 360)
        alt_no_go_angles_C = alter_no_go_angles(no_go_angles_C, current_vector, drift_vector)

        # UPDATE B SEARCH AREA MATRIX
        for i in range(search_diameter):
            for j in range(search_diameter):
                x, y = get_real_coordinates(i, j, shift_vector)

                angle_A_B = angle_between_points(point_A, (x, y))
                angle_C_B = angle_between_points(point_C, (x, y))

                # NO GO ZONE FROM POINT A
                if no_go_angles_A[0] > no_go_angles_A[1]:
                    if angle_A_B > no_go_angles_A[0] or angle_A_B < no_go_angles_A[1]:
                        licit_B_position[i][j] = 0
                elif no_go_angles_A[0] < no_go_angles_A[1]:
                    if no_go_angles_A[0] < angle_A_B < no_go_angles_A[1]:
                        licit_B_position[i][j] = 0

                # ALTERED NO GO ZONE FOR POINT C
                if alt_no_go_angles_C[0] > alt_no_go_angles_C[1]:
                    if angle_C_B > alt_no_go_angles_C[0] or angle_C_B < alt_no_go_angles_C[1]:
                        licit_B_position[i][j] = 0
                elif alt_no_go_angles_C[0] < alt_no_go_angles_C[1]:
                    if alt_no_go_angles_C[0] < angle_C_B < alt_no_go_angles_C[1]:
                        licit_B_position[i][j] = 0

        # RESULT CONTAINERS PREPARATION
        yacht_course_A_B_matrix = values_square(0, search_diameter)  # compass course AB
        distance_A_B_matrix = values_square(0, search_diameter)  # distance AB
        real_speed_A_B_matrix = values_square(0, search_diameter)  # real speed AB
        time_A_B_matrix = values_square(0, search_diameter)  # time of AB journey

        yacht_course_B_C_matrix = values_square(0, search_diameter)  # compass course BC
        distance_B_C_matrix = values_square(0, search_diameter)  # distance BC
        real_speed_B_C_matrix = values_square(0, search_diameter)  # real speed BC
        time_B_C_matrix = values_square(0, search_diameter)  # time of BC journey

        # FOR EVERY POSSIBLE B POINT
        for i in range(search_diameter):
            for j in range(search_diameter):
                x, y = get_real_coordinates(i, j, shift_vector)

                if licit_B_position[i][j] == 1:
                    point_B = (x, y)

                    # INITIAL CALCULATIONS
                    distance_A_B = distance(point_A, point_B)  # distance between A to B points
                    distance_B_C = distance(point_B, point_C)  # distance between B to C points
                    angle_B_C = round(angle_between_points(point_B, point_C))  # angle of B-C route
                    angle_A_B = round(angle_between_points(point_A, point_B))  # angle of A-B route

                    # CALCULATIONS FOR A-B route
                    for yacht_course in range(361):
                        yacht_speed_A_B_value = polar_data[(yacht_course - wind_angle) % 360][wind_speed]
                        yacht_speed_A_B_vector = vector_coordinates(yacht_course, yacht_speed_A_B_value)
                        resultant_speed_A_B_vector = [yacht_speed_A_B_vector[0] + current_vector[0] + drift_vector[0],
                                                      yacht_speed_A_B_vector[1] + current_vector[1] + drift_vector[1]]
                        resultant_angle_A_B = round(angle_between_points((0, 0), resultant_speed_A_B_vector))

                        # BREAK LOOP IF TRUE
                        if resultant_angle_A_B - angle_A_B == 0:  # if same value break loop
                            break
                        # if angle not found yacht course = 360 means true value not found

                    yacht_course_A_B = yacht_course

                    # CALCULATE ROUTE A-B PARAMETERS
                    if yacht_course_A_B == 360:
                        yacht_course_A_B_matrix[i][j] = 360
                        distance_A_B_matrix[i][j] = 0
                        real_speed_A_B_matrix[i][j] = 0
                        time_A_B_matrix[i][j] = 0
                    else:
                        yacht_course_A_B_matrix[i][j] = yacht_course_A_B  # compass course
                        distance_A_B_matrix[i][j] = distance_A_B  # distance
                        real_speed_A_B_matrix[i][j] = distance((0, 0), resultant_speed_A_B_vector)  # real speed
                        time_A_B_matrix[i][j] = distance_A_B / real_speed_A_B_matrix[i][j]  # time of journey

                    # CALCULATIONS FOR B-C ROUTE
                    for yacht_course in range(361):
                        yacht_speed_B_C_value = polar_data[(yacht_course - wind_angle) % 360][wind_speed]
                        yacht_speed_B_C_vector = vector_coordinates(yacht_course, yacht_speed_B_C_value)
                        resultant_speed_B_C_vector = [yacht_speed_B_C_vector[0] + current_vector[0] + drift_vector[0],
                                                      yacht_speed_B_C_vector[1] + current_vector[1] + drift_vector[1]]
                        calculated_angle_B_C = round(angle_between_points((0, 0), resultant_speed_B_C_vector))

                        # BREAK LOOP IF TRUE
                        if calculated_angle_B_C - angle_B_C == 0:  # if same value break loop
                            break

                    yacht_course_B_C = yacht_course

                    # CALCULATE ROUTE B-C PARAMETERS
                    if yacht_course_B_C == 360:
                        yacht_course_B_C_matrix[i][j] = 360
                        distance_B_C_matrix[i][j] = 0
                        real_speed_B_C_matrix[i][j] = 0
                        time_B_C_matrix[i][j] = 0
                    else:
                        yacht_course_B_C_matrix[i][j] = yacht_course_B_C  # compass course
                        distance_B_C_matrix[i][j] = distance_B_C  # distance
                        real_speed_B_C_matrix[i][j] = distance((0, 0), resultant_speed_B_C_vector)  # real speed
                        time_B_C_matrix[i][j] = distance_B_C / real_speed_B_C_matrix[i][j]  # time of journey

        # TIME CALCULATION
        # prepare matrix with summary A-B-C route time for every B point
        total_time_values = [[time_A_B_matrix[i][j] + time_B_C_matrix[i][j] for j in range(search_diameter)] for i in
                             range(search_diameter)]
        total_time = max(max(total_time_values))  # final time of route
        index_I = 0
        index_J = 0

        # find shortest time and calculate point B
        for i in range(search_diameter):
            for j in range(search_diameter):
                if 0 < total_time_values[i][j] < total_time and licit_B_position[i][j] == 1 and \
                        yacht_course_A_B_matrix[i][j] < 360 and yacht_course_B_C_matrix[i][j] < 360:
                    if no_go_angles_A[0] > no_go_angles_A[1]:
                        if not (yacht_course_B_C_matrix[i][j] >= no_go_angles_A[0] or yacht_course_B_C_matrix[i][j] <=
                                no_go_angles_A[1]):
                            total_time = total_time_values[i][j]
                            index_I = i
                            index_J = j
                    elif no_go_angles_A[0] < no_go_angles_A[1]:
                        if not (no_go_angles_A[0] <= yacht_course_B_C_matrix[i][j] <= no_go_angles_A[1]):
                            total_time = total_time_values[i][j]
                            index_I = i
                            index_J = j

        point_B = get_real_coordinates(index_I, index_J, shift_vector)
        yacht_course_A_B = yacht_course_A_B_matrix[index_I][index_J]
        yacht_course_B_C = yacht_course_B_C_matrix[index_I][index_J]
        time_A_B = time_A_B_matrix[index_I][index_J]
        time_B_C = time_B_C_matrix[index_I][index_J]

        if time_A_B <= 0 or time_B_C <= 0:
            search_radius = 2 * search_radius
    # end of while loop

    distance_A_B = distance(point_A, point_B)  # distance between A and B points
    real_speed_A_B = distance_A_B / time_A_B  # speed on A-B route

    distance_B_C = distance(point_B, point_C)  # distance between B and C points
    real_speed_B_C = distance_B_C / time_B_C  # speed on B-C route

    # limits for plotter
    xlim_left = point_A[0] - search_radius
    xlim_right = point_A[0] + search_radius
    ylim_bottom = point_A[1] - search_radius
    ylim_top = point_A[1] + search_radius

    limits = (xlim_left, xlim_right, ylim_bottom, ylim_top)

    from data_models import Algorithm_Outputs

    # prepare outputs
    return Algorithm_Outputs(yacht_course_A_B, real_speed_A_B, time_A_B, point_B, yacht_course_B_C, real_speed_B_C,
                             time_B_C, limits, point_A, point_C, no_go_angles_A)

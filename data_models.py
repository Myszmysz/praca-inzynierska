class Algorithm_Preconditions(object):
    def __init__(self, point_A, wind, current, polar_data):
        self.point_A = point_A
        self.wind_speed = wind[0]
        self.wind_angle = wind[1]
        self.current_speed = current[0]
        self.current_angle = current[1]
        self.polar_data = polar_data


class Algorithm_Outputs(object):
    def __init__(self, yacht_course_A_B, real_speed_A_B, time_A_B, point_B, yacht_course_B_C, real_speed_B_C, time_B_C,
                 limits, point_A, point_C, no_go_angles_A):
        self.yacht_course_A_B = yacht_course_A_B
        self.real_speed_A_B = real_speed_A_B
        self.time_A_B = time_A_B
        self.yacht_course_B_C = yacht_course_B_C
        self.real_speed_B_C = real_speed_B_C
        self.time_B_C = time_B_C
        self.limits = limits
        self.point_B = point_B
        self.point_A = point_A
        self.point_C = point_C
        self.no_go_angles_A = no_go_angles_A
        self.total_time = time_A_B + time_B_C
        self.distance_A_B = time_A_B * real_speed_A_B
        self.distance_B_C = time_B_C * real_speed_B_C
        self.total_distance = self.distance_A_B + self.distance_B_C

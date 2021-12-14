from data_models import Algorithm_Preconditions


class InputError(Exception):
    pass


def read_input_data(input_data_file_name, polar_data_file_name):
    try:
        polar_data = read_polar_from_file(polar_data_file_name)
    except FileNotFoundError:
        raise InputError("Polar data file with name:'" + polar_data_file_name + "' not found")
    except ValueError:
        raise InputError("Incorrect polar data values in polar data file")
    try:
        point_A, wind, current = read_input_from_file(input_data_file_name)
    except FileNotFoundError:
        raise InputError("Input data file with name:'" + input_data_file_name + "' not found")
    except ValueError:
        raise InputError("Incorrect input data values in input data file")

    return Algorithm_Preconditions(point_A, wind, current, polar_data)


def read_input_from_file(input_data_file_name):
    input_data = []
    with open(input_data_file_name, mode="r") as file:
        lines = file.readlines()
        for line in lines:
            input_data.append(line.rstrip("\n"))
        for i, line in enumerate(input_data):
            input_data[i] = line.split(" ")
            if input_data[i][0] == "point_A":
                point_A = ((int(input_data[i][1])), int(input_data[i][2]))
            if input_data[i][0] == "wind":
                wind = ((int(input_data[i][1])), int(input_data[i][2]))
            if input_data[i][0] == "current":
                current = ((float(input_data[i][1])), int(input_data[i][2]))
    return point_A, wind, current


def read_polar_from_file(polar_data_file_name):
    polar_data = []
    with open(polar_data_file_name, mode="r") as f:
        lines = f.readlines()
        for line in lines:
            str_list = line.split('\t')
            num_list = []
            for num in str_list:
                num_list.append(float(num))
            polar_data.append(num_list)
    return polar_data

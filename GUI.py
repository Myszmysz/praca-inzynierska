
from PyQt5 import QtCore, QtGui, QtWidgets
import algorithm
from data_models import *
import plot
from file_operations import *


class Ui_Dialog(object):
    def __init__(self):
        self.algorithm_preconditions = None
        self.algorithm_outputs = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Route Calculator")
        Dialog.resize(999, 664)
        self.calculate_button = QtWidgets.QPushButton(Dialog)
        self.calculate_button.setGeometry(QtCore.QRect(820, 400, 141, 31))
        self.calculate_button.setObjectName("calculate_button")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(570, 350, 421, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(570, 480, 431, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(580, 390, 161, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.point_C_y_label = QtWidgets.QLabel(self.layoutWidget)
        self.point_C_y_label.setObjectName("point_C_y_label")
        self.gridLayout_6.addWidget(self.point_C_y_label, 1, 3, 1, 1)
        self.point_C_x = QtWidgets.QLineEdit(self.layoutWidget)
        self.point_C_x.setObjectName("point_C_x")
        self.gridLayout_6.addWidget(self.point_C_x, 1, 0, 1, 1)
        self.point_C_x_label = QtWidgets.QLabel(self.layoutWidget)
        self.point_C_x_label.setObjectName("point_C_x_label")
        self.gridLayout_6.addWidget(self.point_C_x_label, 1, 1, 1, 1)
        self.target_coordinates_label = QtWidgets.QLabel(self.layoutWidget)
        self.target_coordinates_label.setObjectName("target_coordinates_label")
        self.gridLayout_6.addWidget(self.target_coordinates_label, 0, 0, 1, 4)
        self.point_C_y = QtWidgets.QLineEdit(self.layoutWidget)
        self.point_C_y.setObjectName("point_C_y")
        self.gridLayout_6.addWidget(self.point_C_y, 1, 2, 1, 1)
        self.import_data_button = QtWidgets.QPushButton(Dialog)
        self.import_data_button.setGeometry(QtCore.QRect(820, 290, 141, 31))
        self.import_data_button.setObjectName("import_data_button")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(580, 270, 215, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.actual_position_x_label = QtWidgets.QLabel(self.layoutWidget1)
        self.actual_position_x_label.setObjectName("actual_position_x_label")
        self.gridLayout_7.addWidget(self.actual_position_x_label, 1, 1, 1, 1)
        self.point_A_y = QtWidgets.QLineEdit(self.layoutWidget1)
        self.point_A_y.setObjectName("point_A_y")
        self.gridLayout_7.addWidget(self.point_A_y, 1, 2, 1, 1)
        self.actual_position_y_label = QtWidgets.QLabel(self.layoutWidget1)
        self.actual_position_y_label.setObjectName("actual_position_y_label")
        self.gridLayout_7.addWidget(self.actual_position_y_label, 1, 3, 1, 1)
        self.point_A_x = QtWidgets.QLineEdit(self.layoutWidget1)
        self.point_A_x.setObjectName("point_A_x")
        self.gridLayout_7.addWidget(self.point_A_x, 1, 0, 1, 1)
        self.actual_position_label = QtWidgets.QLabel(self.layoutWidget1)
        self.actual_position_label.setObjectName("actual_position_label")
        self.gridLayout_7.addWidget(self.actual_position_label, 0, 0, 1, 2)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 520, 241, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.point_B_label = QtWidgets.QLabel(self.layoutWidget2)
        self.point_B_label.setObjectName("point_B_label")
        self.gridLayout_8.addWidget(self.point_B_label, 0, 0, 1, 1)
        self.point_B_x = QtWidgets.QLineEdit(self.layoutWidget2)
        self.point_B_x.setObjectName("point_B_x")
        self.gridLayout_8.addWidget(self.point_B_x, 0, 1, 1, 1)
        self.point_B_x_label = QtWidgets.QLabel(self.layoutWidget2)
        self.point_B_x_label.setObjectName("point_B_x_label")
        self.gridLayout_8.addWidget(self.point_B_x_label, 0, 2, 1, 1)
        self.point_B_y = QtWidgets.QLineEdit(self.layoutWidget2)
        self.point_B_y.setObjectName("point_B_y")
        self.gridLayout_8.addWidget(self.point_B_y, 0, 3, 1, 1)
        self.point_B_y_label = QtWidgets.QLabel(self.layoutWidget2)
        self.point_B_y_label.setObjectName("point_B_y_label")
        self.gridLayout_8.addWidget(self.point_B_y_label, 0, 4, 1, 1)
        self.info_box = QtWidgets.QPlainTextEdit(Dialog)
        self.info_box.setGeometry(QtCore.QRect(10, 610, 911, 71))
        self.info_box.setObjectName("info_box")
        self.plotter_graphic = QtWidgets.QLabel(Dialog)
        self.plotter_graphic.setGeometry(QtCore.QRect(0, 0, 571, 511))
        self.plotter_graphic.setObjectName("plotter_graphic")
        self.wind_graphic = QtWidgets.QLabel(Dialog)
        self.wind_graphic.setGeometry(QtCore.QRect(580, 10, 181, 181))
        self.wind_graphic.setObjectName("wind_graphic")
        self.current_graphic = QtWidgets.QLabel(Dialog)
        self.current_graphic.setGeometry(QtCore.QRect(780, 10, 181, 181))
        self.current_graphic.setObjectName("current_graphic")
        self.layoutWidget3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(582, 202, 195, 48))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.wind_speed_label = QtWidgets.QLabel(self.layoutWidget3)
        self.wind_speed_label.setObjectName("wind_speed_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.wind_speed_label)
        self.wind_speed = QtWidgets.QLineEdit(self.layoutWidget3)
        self.wind_speed.setObjectName("wind_speed")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.wind_speed)
        self.wind_angle_label = QtWidgets.QLabel(self.layoutWidget3)
        self.wind_angle_label.setObjectName("wind_angle_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.wind_angle_label)
        self.wind_angle = QtWidgets.QLineEdit(self.layoutWidget3)
        self.wind_angle.setObjectName("wind_angle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.wind_angle)
        self.layoutWidget4 = QtWidgets.QWidget(Dialog)
        self.layoutWidget4.setGeometry(QtCore.QRect(784, 201, 208, 48))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget4)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.current_speed_label = QtWidgets.QLabel(self.layoutWidget4)
        self.current_speed_label.setObjectName("current_speed_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.current_speed_label)
        self.current_speed = QtWidgets.QLineEdit(self.layoutWidget4)
        self.current_speed.setObjectName("current_speed")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.current_speed)
        self.current_angle_label = QtWidgets.QLabel(self.layoutWidget4)
        self.current_angle_label.setObjectName("current_angle_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.current_angle_label)
        self.current_angle = QtWidgets.QLineEdit(self.layoutWidget4)
        self.current_angle.setObjectName("current_angle")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.current_angle)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 550, 911, 48))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.time_to_tack_label = QtWidgets.QLabel(self.widget)
        self.time_to_tack_label.setObjectName("time_to_tack_label")
        self.gridLayout.addWidget(self.time_to_tack_label, 0, 0, 1, 1)
        self.time_A_B = QtWidgets.QLineEdit(self.widget)
        self.time_A_B.setObjectName("time_A_B")
        self.gridLayout.addWidget(self.time_A_B, 0, 1, 1, 1)
        self.distance_to_tack_label = QtWidgets.QLabel(self.widget)
        self.distance_to_tack_label.setObjectName("distance_to_tack_label")
        self.gridLayout.addWidget(self.distance_to_tack_label, 0, 2, 1, 1)
        self.distance_A_B = QtWidgets.QLineEdit(self.widget)
        self.distance_A_B.setObjectName("distance_A_B")
        self.gridLayout.addWidget(self.distance_A_B, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)
        self.course_A_B = QtWidgets.QLineEdit(self.widget)
        self.course_A_B.setObjectName("course_A_B")
        self.gridLayout.addWidget(self.course_A_B, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)
        self.speed_A_B = QtWidgets.QLineEdit(self.widget)
        self.speed_A_B.setObjectName("speed_A_B")
        self.gridLayout.addWidget(self.speed_A_B, 0, 7, 1, 1)
        self.total_time_label = QtWidgets.QLabel(self.widget)
        self.total_time_label.setObjectName("total_time_label")
        self.gridLayout.addWidget(self.total_time_label, 1, 0, 1, 1)
        self.total_time = QtWidgets.QLineEdit(self.widget)
        self.total_time.setObjectName("total_time")
        self.gridLayout.addWidget(self.total_time, 1, 1, 1, 1)
        self.tota_distance_label = QtWidgets.QLabel(self.widget)
        self.tota_distance_label.setObjectName("tota_distance_label")
        self.gridLayout.addWidget(self.tota_distance_label, 1, 2, 1, 1)
        self.total_distance = QtWidgets.QLineEdit(self.widget)
        self.total_distance.setObjectName("total_distance")
        self.gridLayout.addWidget(self.total_distance, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 4, 1, 1)
        self.course_B_C = QtWidgets.QLineEdit(self.widget)
        self.course_B_C.setText("")
        self.course_B_C.setObjectName("course_B_C")
        self.gridLayout.addWidget(self.course_B_C, 1, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 6, 1, 1)
        self.speed_B_C = QtWidgets.QLineEdit(self.widget)
        self.speed_B_C.setText("")
        self.speed_B_C.setObjectName("speed_B_C")
        self.gridLayout.addWidget(self.speed_B_C, 1, 7, 1, 1)

        # disable inputs
        self.wind_speed.setReadOnly(True)
        self.wind_angle.setReadOnly(True)
        self.current_speed.setReadOnly(True)
        self.current_angle.setReadOnly(True)
        self.point_A_x.setReadOnly(True)
        self.point_A_y.setReadOnly(True)

        # disable outputs
        self.total_time.setReadOnly(True)
        self.total_distance.setReadOnly(True)
        self.point_B_x.setReadOnly(True)
        self.point_B_y.setReadOnly(True)
        self.distance_A_B.setReadOnly(True)
        self.time_A_B.setReadOnly(True)
        self.course_A_B.setReadOnly(True)
        self.course_B_C.setReadOnly(True)
        self.speed_A_B.setReadOnly(True)
        self.speed_B_C.setReadOnly(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Route Calculator"))
        self.calculate_button.setText(_translate("Dialog", "calculate"))
        self.point_C_y_label.setText(_translate("Dialog", "y"))
        self.point_C_x_label.setText(_translate("Dialog", "x"))
        self.target_coordinates_label.setText(_translate("Dialog", "target coordinates"))
        self.import_data_button.setText(_translate("Dialog", "import data"))
        self.actual_position_x_label.setText(_translate("Dialog", "x"))
        self.actual_position_y_label.setText(_translate("Dialog", "y"))
        self.actual_position_label.setText(_translate("Dialog", "actual position"))
        self.point_B_label.setText(_translate("Dialog", "tack/gybe location"))
        self.point_B_x_label.setText(_translate("Dialog", "x"))
        self.point_B_y_label.setText(_translate("Dialog", "y"))
        self.plotter_graphic.setText(_translate("Dialog", ""))
        self.wind_graphic.setText(_translate("Dialog", ""))
        self.current_graphic.setText(_translate("Dialog", ""))
        self.wind_speed_label.setText(_translate("Dialog", "wind speed"))
        self.wind_angle_label.setText(_translate("Dialog", "wind angle"))
        self.current_speed_label.setText(_translate("Dialog", "current speed"))
        self.current_angle_label.setText(_translate("Dialog", "current angle"))
        self.time_to_tack_label.setText(_translate("Dialog", "time left to tack/gybe"))
        self.distance_to_tack_label.setText(_translate("Dialog", "distance to tack/gybe"))
        self.label.setText(_translate("Dialog", "suggested course"))
        self.label_4.setText(_translate("Dialog", "real speed before tack/gybe"))
        self.total_time_label.setText(_translate("Dialog", "total time to target"))
        self.tota_distance_label.setText(_translate("Dialog", "total distance"))
        self.label_2.setText(_translate("Dialog", "course after tack/gybe"))
        self.label_3.setText(_translate("Dialog", "real speed after tack/gybe"))

    def addEventListeners(self):
        # event listeners
        self.import_data_button.clicked.connect(self.on_click_import_button)
        self.calculate_button.clicked.connect(self.on_click_calculate)

    def on_click_import_button(self):
        self.clear_info_box()
        try:
            self.algorithm_preconditions = read_input_data("input_data.txt", "polar_data.txt")
        except InputError as error:
            self.print_info_box_message(str(error))
            return

        # info box
        self.print_info_box_message("input data imported successfully")

        # print inputs from file
        self.wind_speed.setText(str(self.algorithm_preconditions.wind_speed) + " kn")
        self.wind_angle.setText(str(self.algorithm_preconditions.wind_angle) + "°")
        self.current_speed.setText(str(self.algorithm_preconditions.current_speed) + " kn")
        self.current_angle.setText(str(self.algorithm_preconditions.current_angle) + "°")
        self.point_A_x.setText(str(self.algorithm_preconditions.point_A[0]))
        self.point_A_y.setText(str(self.algorithm_preconditions.point_A[1]))

        # indicators
        wind_graphic_name = plot.create_indicator(self.algorithm_preconditions.wind_angle, 'r', 'wind_indicator.png')
        self.wind_graphic.setScaledContents(1)
        self.wind_graphic.setPixmap(QtGui.QPixmap(wind_graphic_name))

        current_graphic_name = plot.create_indicator(self.algorithm_preconditions.current_angle, 'g',
                                                     'current_indicator.png')
        self.current_graphic.setScaledContents(1)
        self.current_graphic.setPixmap(QtGui.QPixmap(current_graphic_name))

    def on_click_calculate(self):
        self.clear_info_box()
        self.print_info_box_message("computing in progress")
        # read point C coordinates
        try:
            point_C = (int(self.point_C_x.text()), int(self.point_C_y.text()))
        except ValueError:
            self.print_info_box_message("incorrect coordinates")
            return

        # check if input data is imported
        if self.algorithm_preconditions is None:
            self.print_info_box_message("input data not imported")
            return

        # calculate
        self.calculate_button.setEnabled(False)

        try:
            self.algorithm_outputs = algorithm.algorithm(point_C, self.algorithm_preconditions)
        except algorithm.InputDataError as error:
            self.print_info_box_message(str(error))
            self.calculate_button.setEnabled(True)
            return
        self.calculate_button.setEnabled(True)
        self.print_info_box_message("computing succeed for target point ("+str(point_C[0])+","+str(point_C[1])+")")

        # create plot picture
        plot_file_name = plot.create_plot(self.algorithm_outputs)

        # print outputs
        self.total_time.setText(str(round(self.algorithm_outputs.total_time, 2)) + " h")
        self.total_distance.setText(str(round(self.algorithm_outputs.total_distance, 2)) + " NM")
        self.point_B_x.setText(str(self.algorithm_outputs.point_B[0]))
        self.point_B_y.setText(str(self.algorithm_outputs.point_B[1]))
        self.distance_A_B.setText(str(round(self.algorithm_outputs.distance_A_B, 2)) + " NM")
        self.time_A_B.setText(str(round(self.algorithm_outputs.time_A_B, 2)) + " h")
        self.course_A_B.setText(str(self.algorithm_outputs.yacht_course_A_B) + "°")
        self.course_B_C.setText(str(self.algorithm_outputs.yacht_course_B_C) + "°")
        self.speed_A_B.setText(str(round(self.algorithm_outputs.real_speed_A_B, 2)) + " kn")
        self.speed_B_C.setText(str(round(self.algorithm_outputs.real_speed_B_C, 2)) + " kn")

        # graphics
        self.plotter_graphic.setPixmap(QtGui.QPixmap(plot_file_name))

    def clear_info_box(self):
        self.info_box.setPlainText("")

    def print_info_box_message(self, message):
        self.info_box.setPlainText(message)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.addEventListeners()
    Dialog.show()
    sys.exit(app.exec_())

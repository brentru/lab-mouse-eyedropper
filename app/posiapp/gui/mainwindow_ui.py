# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/brentrubell/Desktop/github_brentru/lab-mouse-eyedropper/app/posiapp/gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 642)
        MainWindow.setAnimated(True)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 151, 101))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 131, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_x_left = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_x_left.setObjectName("btn_x_left")
        self.verticalLayout.addWidget(self.btn_x_left)
        self.btn_x_right = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_x_right.setObjectName("btn_x_right")
        self.verticalLayout.addWidget(self.btn_x_right)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_5.setGeometry(QtCore.QRect(160, 110, 171, 91))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox_5)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 20, 151, 66))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btn_syr_in = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.btn_syr_in.setObjectName("btn_syr_in")
        self.verticalLayout_7.addWidget(self.btn_syr_in)
        self.btn_syr_out = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.btn_syr_out.setObjectName("btn_syr_out")
        self.verticalLayout_7.addWidget(self.btn_syr_out)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 151, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 131, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_y_up = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_y_up.setObjectName("btn_y_up")
        self.verticalLayout_3.addWidget(self.btn_y_up)
        self.btn_y_down = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_y_down.setObjectName("btn_y_down")
        self.verticalLayout_3.addWidget(self.btn_y_down)
        self.btn_quit = QtWidgets.QPushButton(self.centralWidget)
        self.btn_quit.setGeometry(QtCore.QRect(290, 540, 41, 31))
        self.btn_quit.setObjectName("btn_quit")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 210, 281, 121))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self._label_machine_status = QtWidgets.QLabel(self.groupBox_3)
        self._label_machine_status.setGeometry(QtCore.QRect(10, 30, 121, 21))
        self._label_machine_status.setObjectName("_label_machine_status")
        self.label_firmware_ver = QtWidgets.QLabel(self.groupBox_3)
        self.label_firmware_ver.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label_firmware_ver.setObjectName("label_firmware_ver")
        self.label_port = QtWidgets.QLabel(self.groupBox_3)
        self.label_port.setGeometry(QtCore.QRect(10, 80, 261, 31))
        self.label_port.setObjectName("label_port")
        self.label_machine_status = QtWidgets.QLabel(self.groupBox_3)
        self.label_machine_status.setGeometry(QtCore.QRect(120, 30, 121, 21))
        self.label_machine_status.setText("")
        self.label_machine_status.setObjectName("label_machine_status")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_6.setGeometry(QtCore.QRect(160, 20, 171, 91))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.groupBox_6)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(10, 20, 151, 66))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.btn_platform_right = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.btn_platform_right.setObjectName("btn_platform_right")
        self.verticalLayout_8.addWidget(self.btn_platform_right)
        self.btn_platform_left = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.btn_platform_left.setObjectName("btn_platform_left")
        self.verticalLayout_8.addWidget(self.btn_platform_left)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 330, 291, 151))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label_5.setObjectName("label_5")
        self.comboBox_Ports = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_Ports.setGeometry(QtCore.QRect(80, 20, 104, 41))
        self.comboBox_Ports.setObjectName("comboBox_Ports")
        self.comboBox_Ports.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 111, 21))
        self.label_6.setObjectName("label_6")
        self.btn_refresh_ports = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_refresh_ports.setGeometry(QtCore.QRect(190, 20, 91, 41))
        self.btn_refresh_ports.setObjectName("btn_refresh_ports")
        self.pushButton_motors_off = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_motors_off.setGeometry(QtCore.QRect(0, 80, 101, 41))
        self.pushButton_motors_off.setObjectName("pushButton_motors_off")
        self.label_steps_set = QtWidgets.QLabel(self.groupBox_7)
        self.label_steps_set.setGeometry(QtCore.QRect(120, 60, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_steps_set.setFont(font)
        self.label_steps_set.setObjectName("label_steps_set")
        self.pushButton_disconnect = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_disconnect.setGeometry(QtCore.QRect(90, 80, 101, 41))
        self.pushButton_disconnect.setObjectName("pushButton_disconnect")
        self.pushButton_rst = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_rst.setGeometry(QtCore.QRect(90, 110, 101, 41))
        self.pushButton_rst.setObjectName("pushButton_rst")
        self.btn_conn = QtWidgets.QPushButton(self.groupBox_7)
        self.btn_conn.setGeometry(QtCore.QRect(190, 50, 91, 41))
        self.btn_conn.setObjectName("btn_conn")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 480, 111, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 30, 31, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 50, 41, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 50, 31, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 70, 31, 21))
        self.pushButton_8.setObjectName("pushButton_8")
        self.groupBox_camera = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_camera.setGeometry(QtCore.QRect(350, 0, 211, 291))
        self.groupBox_camera.setObjectName("groupBox_camera")
        self.btn_cam1_start = QtWidgets.QPushButton(self.groupBox_camera)
        self.btn_cam1_start.setGeometry(QtCore.QRect(10, 240, 91, 31))
        self.btn_cam1_start.setObjectName("btn_cam1_start")
        self.btn_cam1_pause = QtWidgets.QPushButton(self.groupBox_camera)
        self.btn_cam1_pause.setGeometry(QtCore.QRect(110, 240, 91, 31))
        self.btn_cam1_pause.setObjectName("btn_cam1_pause")
        self.btn_cam1_screenshot = QtWidgets.QPushButton(self.groupBox_camera)
        self.btn_cam1_screenshot.setGeometry(QtCore.QRect(60, 260, 91, 31))
        self.btn_cam1_screenshot.setObjectName("btn_cam1_screenshot")
        self.lbl_cam1 = QtWidgets.QLabel(self.groupBox_camera)
        self.lbl_cam1.setGeometry(QtCore.QRect(10, 30, 191, 211))
        self.lbl_cam1.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_cam1.setText("")
        self.lbl_cam1.setObjectName("lbl_cam1")
        self.lbl_cam_1_activity = QtWidgets.QLabel(self.groupBox_camera)
        self.lbl_cam_1_activity.setGeometry(QtCore.QRect(180, -10, 81, 41))
        self.lbl_cam_1_activity.setObjectName("lbl_cam_1_activity")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 480, 161, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.groupBox_camera_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_camera_2.setGeometry(QtCore.QRect(350, 290, 211, 291))
        self.groupBox_camera_2.setObjectName("groupBox_camera_2")
        self.btn_cam1_start_4 = QtWidgets.QPushButton(self.groupBox_camera_2)
        self.btn_cam1_start_4.setGeometry(QtCore.QRect(10, 240, 91, 31))
        self.btn_cam1_start_4.setObjectName("btn_cam1_start_4")
        self.btn_cam1_stop_4 = QtWidgets.QPushButton(self.groupBox_camera_2)
        self.btn_cam1_stop_4.setGeometry(QtCore.QRect(110, 240, 91, 31))
        self.btn_cam1_stop_4.setObjectName("btn_cam1_stop_4")
        self.btn_cam1_screenshot_4 = QtWidgets.QPushButton(self.groupBox_camera_2)
        self.btn_cam1_screenshot_4.setGeometry(QtCore.QRect(60, 260, 91, 31))
        self.btn_cam1_screenshot_4.setObjectName("btn_cam1_screenshot_4")
        self.lbl_cam1_4 = QtWidgets.QLabel(self.groupBox_camera_2)
        self.lbl_cam1_4.setGeometry(QtCore.QRect(10, 30, 191, 211))
        self.lbl_cam1_4.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_cam1_4.setText("")
        self.lbl_cam1_4.setObjectName("lbl_cam1_4")
        self.lbl_cam_1_activity_4 = QtWidgets.QLabel(self.groupBox_camera_2)
        self.lbl_cam_1_activity_4.setGeometry(QtCore.QRect(180, -10, 81, 41))
        self.lbl_cam_1_activity_4.setObjectName("lbl_cam_1_activity_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 577, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuPositioner = QtWidgets.QMenu(self.menuBar)
        self.menuPositioner.setObjectName("menuPositioner")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuPositioner.addSeparator()
        self.menuPositioner.addAction(self.actionFile)
        self.menuPositioner.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuPositioner.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Positioner Panel"))
        self.groupBox.setTitle(_translate("MainWindow", "X-Axis"))
        self.btn_x_left.setText(_translate("MainWindow", "Left"))
        self.btn_x_right.setText(_translate("MainWindow", "Right"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Syringe"))
        self.btn_syr_in.setText(_translate("MainWindow", "Towards Mouse"))
        self.btn_syr_out.setText(_translate("MainWindow", "Away from Mouse"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Y-Axis"))
        self.btn_y_up.setText(_translate("MainWindow", "Up"))
        self.btn_y_down.setText(_translate("MainWindow", "Down"))
        self.btn_quit.setText(_translate("MainWindow", "Quit"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Positioner Status"))
        self._label_machine_status.setText(_translate("MainWindow", "Machine Status:"))
        self.label_firmware_ver.setText(_translate("MainWindow", "Firmware Ver.:"))
        self.label_port.setText(_translate("MainWindow", "Port:"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Platform "))
        self.btn_platform_right.setText(_translate("MainWindow", "Rotate Right"))
        self.btn_platform_left.setText(_translate("MainWindow", "Rotate Left"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Quick Settings"))
        self.label_5.setText(_translate("MainWindow", "Select Port: "))
        self.comboBox_Ports.setItemText(0, _translate("MainWindow", "..."))
        self.label_6.setText(_translate("MainWindow", "Steps (mm/min):"))
        self.btn_refresh_ports.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_motors_off.setText(_translate("MainWindow", "Motors Off"))
        self.label_steps_set.setText(_translate("MainWindow", "100"))
        self.pushButton_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.pushButton_rst.setText(_translate("MainWindow", "Reset"))
        self.btn_conn.setText(_translate("MainWindow", "Connect"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Motion Presets"))
        self.pushButton_3.setText(_translate("MainWindow", "PS1"))
        self.pushButton_4.setText(_translate("MainWindow", "set"))
        self.pushButton_5.setText(_translate("MainWindow", "PS2"))
        self.pushButton_6.setText(_translate("MainWindow", "PS3"))
        self.pushButton_7.setText(_translate("MainWindow", "set"))
        self.pushButton_8.setText(_translate("MainWindow", "set"))
        self.groupBox_camera.setTitle(_translate("MainWindow", "Video Feed 1"))
        self.btn_cam1_start.setText(_translate("MainWindow", "start"))
        self.btn_cam1_pause.setText(_translate("MainWindow", "pause"))
        self.btn_cam1_screenshot.setText(_translate("MainWindow", "screenshot"))
        self.lbl_cam_1_activity.setText(_translate("MainWindow", "Idle"))
        self.pushButton.setText(_translate("MainWindow", "EMERGENCY STOP"))
        self.groupBox_camera_2.setTitle(_translate("MainWindow", "Video Feed 2"))
        self.btn_cam1_start_4.setText(_translate("MainWindow", "start"))
        self.btn_cam1_stop_4.setText(_translate("MainWindow", "stop"))
        self.btn_cam1_screenshot_4.setText(_translate("MainWindow", "screenshot"))
        self.lbl_cam_1_activity_4.setText(_translate("MainWindow", "Idle"))
        self.menuPositioner.setTitle(_translate("MainWindow", "Positioner"))
        self.actionFile.setText(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))


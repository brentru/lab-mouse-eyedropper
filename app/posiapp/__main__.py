import sys
import time
import cv2
import serial
from serial import SerialException
import serial.tools.list_ports
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

from .gui.mainwindow_ui import Ui_MainWindow

# consts
BAUD = 250000
is_connected = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.image = None
        # connect primary axis control buttons
        self.conn_btn_axis()
        # connect control buttons
        self.connect_btns_controls()

        # vision system
        self.btn_cam1_start.clicked.connect(self.start_webcam_1)
        self.btn_cam1_stop.clicked.connect(self.stop_webcam_1)
        self.btn_cam1_screenshot.clicked.connect(self.screenshot_webcam_1)

    def screenshot_webcam_1(self):
        #todo: fix, doesnt read image in displayImage
        ret, frame = cap2.read()
        cv2.imwrite("cam1.png",frame)
        print('-- captured screenshot')
        cap2.release()

    def start_webcam_1(self):
        self.capture=cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(250)

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.image = cv2.flip(self.image,1)
        self.displayImage(self.image,1)

    def stop_webcam_1(self):
        self.timer.stop()

    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        if window == 1:
            self.lbl_cam1.setPixmap(QPixmap.fromImage(outImage))
            self.lbl_cam1.setScaledContents(True)

    def connect_btns_controls(self):
        self.btn_refresh_ports.clicked.connect(self.list_serial_ports)
        self.btn_conn.clicked.connect(self.connect_machine)
        self.btn_quit.clicked.connect(self.dc_and_exit)
        # self.btn_cam1_start.clicked.connect(self.cam_1_start)
        # self.btn_cam1_stop.clicked.connect(self.cam_1_stop)

    def conn_btn_axis(self):
    # x-axis
        self.btn_x_right.clicked.connect(lambda: self.move_axis('xRight'))
        self.btn_x_left.clicked.connect(lambda: self.move_axis('xLeft'))
    # y-axis
        self.btn_y_up.clicked.connect(lambda: self.move_axis('yUp'))
        self.btn_y_down.clicked.connect(lambda: self.move_axis('yDown'))
    # platform
        self.btn_platform_right.clicked.connect(lambda: self.move_axis('platRight'))
        self.btn_platform_left.clicked.connect(lambda: self.move_axis('platLeft'))
    # syringe
        self.btn_syr_out.clicked.connect(lambda: self.move_axis('syrIn'))
        self.btn_syr_in.clicked.connect(lambda: self.move_axis('syrOut'))


    def move_axis(self, axis):
        """identifies axis and sends ID to gcode sender"""
        if axis == 'xRight':
            print("moving x axis right")
        elif axis == 'xLeft':
            print("moving x axis left")
        elif axis == 'yUp':
            print("moving y axis up")
        elif axis == 'yDown':
            print("moving y axis down")
        elif axis == 'platRight':
            print("moving platform right")
        elif axis == 'platLeft':
            print("moving platform left")
        else:
            print("axis un-identified")

    def connect_machine(self):
        """connects the machine to the serial port, if selected"""
        port = self.comboBox_Ports.currentText()
        try:
            self.label_port.setText(port)
        except NameError:
            pass
        serial_port = serial.Serial(port, BAUD)
        try:
            # wake up the serial
            serial_port.write(("\n\r\n\r\n\r".encode()))
            time.sleep(3)
            startup_data = serial_port.readline()
        except serial.serialutil.SerialException as e:
            print(e.errno)
            print(e)
        # check for startup data on the serial
        if serial_port.isOpen():
            self.label_machine_status.setText("is_connected")
            is_connected = 1
            print("* DBG, data on serial, flushing...")
            serial_port.flushInput()
        else:
            serial_port.close()
            print("* DBG, serial port not found, closing...")

    def printOut(self):
        # dbg printing test
        print("* button clicked")


    def list_serial_ports(self):
        """Enumerates USB serial comm. ports and
        adds them to the combobox for selection
        """
        is_connected = [port.device for port in serial.tools.list_ports.comports()]
        is_connected = list(is_connected)
        if len(is_connected) > 1:
            # update combo box with serial device list
            serial_devices = [
                self.tr(is_connected[0]),
                self.tr(is_connected[1]),
            ]
            self.comboBox_Ports.addItems(serial_devices)
        else:
            self.comboBox_Ports.clear()


    def dc_and_exit(self):
        #s.close()
        sys.exit()


class ApplicationActions():
    def exit():
        sys.exit(app.exec_())



def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

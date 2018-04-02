import sys
import time
import cv2
import serial
from serial import SerialException
import serial.tools.list_ports
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow

from .gui.mainwindow_ui import Ui_MainWindow

# consts
BAUD = 250000
IS_CONNECTED = 0


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """init the main window"""
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.image = None
        # connect primary axis control buttons
        self.conn_btn_axis()
        # connect control buttons
        self.connect_btns_controls()


    def take_screenshot(self, camera=0):
        """ grabs the current capture frame
        @int camera: 0 = off, 1 = cam1, 2 = cam2
        """
        if camera == 1:
            ret, self.screenshot = self.cam1_capture.read()
        elif camera == 2:
            ret, self.screenshot = self.cam2_capture.read()
        else:
            print('-- ERR: no camera found')
            pass
        self.screenshot = cv2.flip(self.screenshot, 1)
        self.label_display(self.screenshot, 1)


        # TODO: change imwrite to take in datetime + camera used
        curr_time = time.localtime()
        cv2.imwrite("camera.png", self.screenshot)
        print('-- screenshot captured')


    def start_webcam_1(self):
        """webcam 1 capture setup and config"""
        self.cam1_capture = cv2.VideoCapture(0)
        self.cam1_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cam1_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
        self.lbl_cam_1_activity.setText("LIVE")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(250)


    def update_frame(self):
        """starts capture, every (timer)ms"""
        ret, self.image = self.cam1_capture.read()
        self.image = cv2.flip(self.image, 1)
        self.label_display(self.image, 1)


    def stop_webcam_1(self):
        """stops webcam1 from displaying image frames"""
        self.lbl_cam_1_activity.setText("idle")
        self.timer.stop()


    def label_display(self, img, window=1):
        """image manipulation for label display"""
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        out_image = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        out_image = out_image.rgbSwapped()

        if window == 1:
            self.lbl_cam1.setPixmap(QPixmap.fromImage(out_image))
            self.lbl_cam1.setScaledContents(True)


    def connect_btns_controls(self):
        """connects non-axis-specific buttons to slots"""
        self.btn_refresh_ports.clicked.connect(self.list_serial_ports)
        self.btn_conn.clicked.connect(self.connect_machine)
        self.btn_quit.clicked.connect(self.dc_and_exit)
        # vision system
        self.btn_cam1_start.clicked.connect(self.start_webcam_1)
        self.btn_cam1_stop.clicked.connect(self.stop_webcam_1)
        self.btn_cam1_screenshot.clicked.connect(lambda: self.take_screenshot(1))


    def conn_btn_axis(self):
        """connects axis-specific buttons to slots"""
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
            self.label_machine_status.setText("IS_CONNECTED")
            IS_CONNECTED = 1
            print("* DBG, data on serial, flushing...")
            serial_port.flushInput()
        else:
            serial_port.close()
            print("* DBG, serial port not found, closing...")


    def list_serial_ports(self):
        """Enumerates USB serial comm. ports and
        adds them to the combobox for selection
        """
        IS_CONNECTED = [port.device for port in serial.tools.list_ports.comports()]
        IS_CONNECTED = list(IS_CONNECTED)
        if len(IS_CONNECTED) > 1:
            # update combo box with serial device list
            serial_devices = [
                self.tr(IS_CONNECTED[0]),
                self.tr(IS_CONNECTED[1]),
            ]
            self.comboBox_Ports.addItems(serial_devices)
        else:
            self.comboBox_Ports.clear()


    def dc_and_exit(self):
        #s.close()
        sys.exit()


class ApplicationActions():
    """generalized application controls and handlers"""
    def exit():
        sys.exit(app.exec_())



def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

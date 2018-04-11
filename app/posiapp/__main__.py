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
IS_CONNECTED = 0

class SerCtrl:
    """PySerial communication"""
    def __init__(self, baudrate=250000, timeout=5):
        port_list = [port.device for port in serial.tools.list_ports.comports()]
        print(">    serial ports: ", port_list)
        # set up serial
        self.ser = serial.Serial()
        try:
            self.ser.port = port_list[1]
        except IndexError:
            print("serial port out of range")
        self.ser.baudrate = baudrate
        print(">    serial connected to ", self.ser.port, "at ", self.ser.baudrate)
        print(self.ser)

    def open(self):
        """opens the serial port"""
        print(">    opening serial...")
        try:
            self.ser.open()
            print(">    serial connection opened")
        except:
            print(">    ERROR: serial not opened")

    def close(self):
        """safely close the serial port"""
        self.ser.close()
        print(">    serial closed")

    def write(self, data):
        """send encoded data"""
        data = data + "\n"
        self.ser.write(data.encode())
        print(">    wrote data to serial")


    def read(self):
        """reads 100b from serial"""
        print(self.ser.read(100))


    def read_line(self):
        """reads line of data from serial, prevents blocking"""
        line = self.ser.readline()
        print(">    serial: ", line.decode())


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """init the main window"""
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # image setup
        self.image = None
        # connect primary axis control buttons
        self.conn_btn_axis()
        # connect control buttons
        self.connect_btns_controls()
        # create a serial object
        self.serialObject = SerCtrl()
        self.serialObject.open()
        self.serialObject.write("\n\r\n\r\n")
        time.sleep(3)
        self.serialObject.read_line()
        # setup rel. positioning
        self.serialObject.write("G91")



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


    def pause_webcam(self, webcam=0):
        """stops timer and unloads opencv instance"""
        if webcam == 1:
            self.timer1.stop()
            self.cam1_capture.release()
        elif webcam == 2:
            self.timer2.stop()
            self.cam2_capture.release()
        else:
            print('cam not recognized')
            pass


    def start_webcam(self, camera=0):
        """ camera capture setup and configuration
        @int camera: 0 = off, 1 = cam1, 2 = cam2
        """
        if camera == 1:
            self.cam1_capture = cv2.VideoCapture(1)
            self.cam1_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cam1_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
            self.lbl_cam_1_activity.setText("LIVE")
            self.timer1 = QTimer(self)
            print('--started timer1')
            self.timer1.timeout.connect(self.update_frame)
            self.timer1.start(250)
        elif camera == 2:
            self.cam2_capture = cv2.VideoCapture(2)
            self.cam2_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cam2_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
            #self.lbl_cam_2_activity.setText("LIVE")
            self.timer2 = QTimer(self)
            self.timer2.timeout.connect(self.update_frame_2)
            self.timer2.start(250)
        else:
            print('-- camera not detected')
            pass


    def update_frame(self):
        """CAM1: starts capture, every (timer)ms"""
        ret, self.image = self.cam1_capture.read()
        self.image = cv2.flip(self.image, 1)
        # displaying gridlines
        image_x = int(self.image.shape[1])
        image_y = int(self.image.shape[0])
        # vertical center
        cv2.line(self.image, (int(image_x/2), 0), (int(image_x/2), image_y), (255, 50, 50), 10, 1)
        # vertical left
        cv2.line(self.image, (int(image_x/4), 0), (int(image_x/4), image_y), (255, 50, 50), 10, 1)
        cv2.line(self.image, (0, int(image_y/2)), (image_x, int(image_y/2)), (255, 50, 50), 10, 1)
        cv2.line(self.image, (0, int(image_y/8)), (image_x, int(image_y/8)), (255, 50, 50), 10, 1)
        cv2.line(self.image, (0, int(image_y-150)), (image_x, int(image_y-150)), (255, 50, 50), 10, 1)
        self.label_display(self.image, 1)


    def update_frame_2(self):
        """CAM2: starts capture, every (timer)ms"""
        ret, self.image = self.cam2_capture.read()
        self.image = cv2.flip(self.image, 1)
        # displaying gridlines
        image_x = int(self.image.shape[1])
        image_y = int(self.image.shape[0])
        # vertical center
        cv2.line(self.image, (int(image_x/2), 0), (int(image_x/2), image_y), (255, 50, 50), 10, 1)
        # vertical left
        cv2.line(self.image, (int(image_x/4), 0), (int(image_x/4), image_y), (255, 50, 50), 10, 1)
        cv2.line(self.image, (0, int(image_y/2)), (image_x, int(image_y/2)), (255, 50, 50), 10, 1)
        cv2.line(self.image, (0, int(image_y/8)), (image_x, int(image_y/8)), (255, 50, 50), 10, 1)
        cv2.line(self.image, (0, int(image_y-150)), (image_x, int(image_y-150)), (255, 50, 50), 10, 1)
        # switch this to the cam2 label
        self.label_display(self.image, 2)


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
        elif window == 2:
            self.lbl_cam2.setPixmap(QPixmap.fromImage(out_image))
            self.lbl_cam2.setScaledContents(True)


    def connect_btns_controls(self):
        """connects non-axis-specific buttons to slots"""
        # serial-based buttons
        self.btn_disconnect.clicked.connect(lambda: self.dc_and_exit(0))
        self.btn_quit.clicked.connect(lambda: self.dc_and_exit(1))
        self.btn_estop.clicked.connect(self.emergency_stop)
        self.btn_disable_steppers.clicked.connect(self.disable_steppers)
        # vision system: camera 1
        self.btn_cam1_start.clicked.connect(lambda: self.start_webcam(1))
        self.btn_cam1_pause.clicked.connect(lambda: self.pause_webcam(1))
        self.btn_cam1_screenshot.clicked.connect(lambda: self.take_screenshot(1))
        # vision system: camera 2
        self.btn_cam2_start.clicked.connect(lambda: self.start_webcam(2))
        self.btn_cam2_pause.clicked.connect(lambda: self.pause_webcam(2))
        self.btn_cam2_screenshot.clicked.connect(lambda: self.take_screenshot(2))
        # preset-buttons
        self.btn_ps1_set.clicked.connect(lambda: self.get_position(1))
        self.btn_ps2_set.clicked.connect(lambda: self.get_position(2))
        self.btn_ps3_set.clicked.connect(lambda: self.get_position(3))


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
            self.serialObject.write("G1 X1 F600")
            self.serialObject.read_line()
        elif axis == 'xLeft':
            print("moving x axis left")
            self.serialObject.write("G1 X-1 F600")
            self.serialObject.read_line()
        elif axis == 'yUp':
            print("moving y axis up")
            self.serialObject.write("G1 Y1 F600")
            self.serialObject.read_line()
        elif axis == 'yDown':
            print("moving y axis down")
            self.serialObject.write("G1 Y0 F600")
            self.serialObject.read_line()
        elif axis == 'platRight':
            print("moving platform right")
            self.serialObject.write("G1 Z01 F600")
            self.serialObject.read_line()
        elif axis == 'platLeft':
            print("moving platform left")
            self.serialObject.write("G1 Z-01 F600")
            self.serialObject.read_line()
        else:
            print("axis un-identified")


    def disable_steppers(self):
        """disables all steppers"""
        self.serialObject.write("M18")
        print(">    steppers disabled")


    def get_position(self, preset):
        """gets machine position for presets"""
        if preset == 1:
            self.serialObject.write("M114")
            self.pre1 = self.serialObject.read_line()
            print(">    PRESET1: ", self.pre1)
        elif preset == 2:
            self.serialObject.write("M114")
            self.pre2 = self.serialObject.read_line()
            print(">    PRESET1: ", self.pre2)
        elif preset == 3:
            self.serialObject.write("M114")
            self.pre3 = self.serialObject.read_line()
            print(">    PRESET1: ", self.pre3)


    def emergency_stop(self):
        """stop machine from operating"""
        print(">    EMERGENCY STOP")
        self.disable_steppers()
        # disable ATX power supply
        self.serialObject.write("M81")
        self.SerialObject.close()


    def dc_serial(self):
        """disconnect serial"""
        self.serialObject.close()


    def dc_and_exit(self, dc):
        """disconnect serial and/or exit application
        0: disconnect serial
        1: dc and exit"""
        if dc == 0:
            self.serialObject.close()
        elif dc == 1:
            self.serialObject.close()
            sys.exit()


class ApplicationActions():
    """generalized application controls and handlers"""
    def exit():
        """qt-specific app exit"""
        sys.exit(app.exec_())


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

import glob
import sys
import time

import serial
import serial.tools.list_ports
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

from .gui.mainwindow_ui import Ui_MainWindow

# consts
BAUD = 250000

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # connect primary axis control buttons
        self.connect_btns_primaryAxis()
        # connect control buttons
        self.connect_btns_controls()


    def connect_btns_controls(self):
        self.btn_refresh_ports.clicked.connect(self.listSerialPorts)
        self.btn_conn.clicked.connect(self.connect_machine)
        self.btn_quit.clicked.connect(self.dc_and_exit)
    def connect_btns_primaryAxis(self):
    # x-axis connections
        self.btn_x_left.clicked.connect(self.printOut)
        self.btn_x_right.clicked.connect(self.printOut)
    # y-axis connections
        self.btn_y_up.clicked.connect(self.printOut)
        self.btn_y_down.clicked.connect(self.printOut)
    # TODO: peripheral axis


    def connect_machine(self):
        """connects the machine to the serial port, if selected"""
        port = self.comboBox_Ports.currentText()
        try:
            self.label_port.setText(port)
        except NameError:
            pass
        s = serial.Serial(port, BAUD)
        # wake up the serial
        s.write(("\n\r\n\r\n\r".encode()))
        time.sleep(3)
        startup_data = s.readline()
        # check for startup data on the serial
        if startup_data is not None:
            self.label_machine_status.setText("connected")
            print("* DBG, data on serial, flushing...")
            s.flushInput()
        else:
            s.close()


    def printOut(self):
        # dbg printing test
        print("* button clicked")


    def listSerialPorts(self):
        """Enumerates USB serial comm. ports and
        adds them to the combobox for selection
        """
        connected = [port.device for port in serial.tools.list_ports.comports()]
        connected = list(connected)
        if len(connected) > 1:
            # update combo box with serial device list
            serial_devices = [
            self.tr(connected[0]),
            self.tr(connected[1]),
            ]
            self.comboBox_Ports.addItems(serial_devices)
        else:
            self.comboBox_Ports.clear()


    def dc_and_exit(self):
        s.close()
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

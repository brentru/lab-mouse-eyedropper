import sys
import glob
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

from .gui.mainwindow_ui import Ui_MainWindow

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
    def connect_btns_primaryAxis(self):
    # x-axis connections
        self.btn_x_up.clicked.connect(self.printOut)
        self.btn_x_down.clicked.connect(self.printOut)
        self.btn_x_left.clicked.connect(self.printOut)
        self.btn_x_right.clicked.connect(self.printOut)
    # y-axis connections
        self.btn_y_up.clicked.connect(self.printOut)
        self.btn_y_down.clicked.connect(self.printOut)
        self.btn_y_left.clicked.connect(self.printOut)
        self.btn_y_right.clicked.connect(self.printOut)
    # TODO: z-axis connections


    def printOut(self):
        # dbg printing test
        print("* button clicked")


    def listSerialPorts(self):
        """
        Enumerates USB serial comm. ports and adds them to the combobox
        """
        connected = [port.device for port in serial.tools.list_ports.comports()]
        connected = list(connected)
        if len(connected) > 1:
            # update combo box with serial device list
            serial_devices = [
            self.tr(connected[0]),
            self.tr(connected[1]),
            ]
            self.comboBox.addItems(serial_devices)
        else:
            self.comboBox.clear()



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

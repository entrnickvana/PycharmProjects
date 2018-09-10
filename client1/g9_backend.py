# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nickj\Desktop\ZZZ\g9.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import socket
from threading import Thread

def client_thread(g9_c, ui_arg):
    g9_c.start_client(ui_arg)

class g9Client():

    def start_client(self, ui_arg):
        hostname, sld, tld, port = 'www', 'theberrics', 'com', 80
        target = '{}.{}.{}'.format(hostname, sld, tld)
        
        # create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # connect the client
        # client.connect((target, port))
        client.connect(('127.0.0.1', 1256))
        #client.connect(('192.168.1.129', 1256))
        
        print('connected:\n')
        
        # ------------------- FOR WEB ADDRESSES  ----------------------------------------
        # addr_str = 'GET /index.html HTTP/1.1\r\nHost: {}.{}\r\n\r\n'.format(sld, tld)
        # encoded_str = addr_str.encode()
        
        server_msg = client.recv(1024)
        
        print('past received\n')
        
        print(server_msg)
        
        msg = '&&&& CLIENT BITCH &&&&&&&&\n'
        client.send(msg.encode())        
        # send some data (in this case a HTTP GET request)

        while True:
    
            msg2 = str(ui_arg.verticalSlider.value()) + str(ui_arg.verticalSlider_2.value()) + str(ui_arg.verticalSlider_3.value())
    
            client.send(msg2.encode())
        
        # receive the response data (4096 is recommended buffer size)
        # response = client.recv(4096)
        
        # print(response)

class Ui_Form(object):
    lo = 0
    mid = 0
    hi = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1842, 1274)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalSlider_3 = QtWidgets.QSlider(Form)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.gridLayout.addWidget(self.verticalSlider_3, 1, 2, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(Form)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout.addWidget(self.verticalSlider_2, 1, 1, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(Form)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 1, 0, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 0, 2, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 0, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.verticalSlider.sliderMoved['int'].connect(self.lcdNumber.display)
        self.verticalSlider_2.sliderMoved['int'].connect(self.lcdNumber_2.display)
        self.verticalSlider_3.sliderMoved['int'].connect(self.lcdNumber_3.display)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    @pyqtSlot(int, name='on_verticalSlider_sliderMoved')
    def on_verticalSlider_sliderMoved(self, i):
        lo = i
        print("LO: " + str(lo))        

    @pyqtSlot(int, name='on_verticalSlider_2_sliderMoved')
    def on_verticalSlider_2_sliderMoved(self, i):
        mid = i
        print("LO: " + str(mid))

    @pyqtSlot(int, name='on_verticalSlider_3_sliderMoved')
    def on_verticalSlider_3_sliderMoved(self, i):
        hi = i
        print("LO: " + str(hi))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    g = g9Client()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    thread = Thread(target = client_thread, args = (g, ui))
    thread.start()
    

    sys.exit(app.exec_())

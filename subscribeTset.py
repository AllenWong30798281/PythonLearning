
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QWidget, QSlider, QMainWindow, QPushButton, QLabel, QLineEdit, QInputDialog, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import telnetlib,time,re



class Example(QWidget):


    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        sld = QSlider(Qt.Vertical,self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setValue(50)
        sld.setMaximum(100)
        sld.setMinimum(60)
        sld.setTickInterval(3)
        sld.setTickPosition(QSlider.TicksBothSides)


        self.btn = QPushButton('IP address', self)
        self.btn.move(10, 50)
        self.btn.clicked.connect(self.showDialog)

        self.btnIST = QPushButton('Instance Tag', self)
        self.btnIST.move(10, 100)
        self.btnIST.clicked.connect(self.showDialogIST)

        self.le = QLineEdit(self)
        self.le.move(10, 0)
        self.le.setText('disconnect')
        
        sld.setGeometry(180, 40, 20, 200)
        sld.valueChanged[int].connect(self.changeValue)


        self.setGeometry(300, 300, 320, 300)
        self.setWindowTitle('biamp slider test')
        self.show()
        
####订阅电平值并在shell中显示####
        
        while True:
            global rawMsg
            rawMsg = tn.read_very_eager()
            cookedMsg = re.search(b'! "publishToken":"(.*)" "value":(.*)\r\n',rawMsg)
            level = cookedMsg.group(2).decode("utf-8")
            print("REGEX is " + level)
            time.sleep(1.5)
            
####订阅电平值并在shell中显示####



    def changeValue(self, Svalue):
        
        Svalue = Svalue-100
        value = str(Svalue)
        
        s = InstanceTag + " set level " + level + " " + value + "\n"
        s = s.encode(encoding="utf-8")
        tn.write(s)
        


    def showDialog(self):
        global tn
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter IP address:')

        if ok:
            self.le.setText('connected')
            HOST = str(text)
            

    def showDialogIST(self):
        global InstanceTag
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter Instance Tag:')
        InstanceTag = str(text)

    
        
if __name__ == '__main__':

    HOST = "192.168.6.253"
    ls = b"Level13 toggle mute 1\n"
    InstanceTag = 'Level13'
    level = str(1)
    value = str(0)
    tn = telnetlib.Telnet(HOST)
    tn.set_debuglevel(5)
    tn.read_until(b"Welcome to the Tesira Text Protocol Server...")
    print("telnet connected")
    subs = b"AudioMeter1 subscribe level 1 123 1000\n"
    tn.write(subs)
    rawMsg = tn.read_very_eager()

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


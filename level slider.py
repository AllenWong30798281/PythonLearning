from PyQt5.QtWidgets import (QWidget, QSlider, QMainWindow, QPushButton,QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import telnetlib

HOST = "192.168.6.253"
ls = b"Level13 toggle mute 1\n"
InstanceTag = 'Level13'
level = str(1)
value = str(0)


tn = telnetlib.Telnet(HOST)
tn.read_until(b"Welcome to the Tesira Text Protocol Server...")
print("哈哈哈")



class Example(QWidget):


    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        sld = QSlider(Qt.Vertical, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 20, 200)
        sld.valueChanged[int].connect(self.changeValue)


        self.setGeometry(300, 300, 280, 300)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, Svalue):
        
        Svalue = Svalue-100
        value = str(Svalue)
        
        s = InstanceTag + " set level " + level + " " + value + "\n"
        s = s.encode(encoding="utf-8")
        tn.write(s)
        
        """if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('med.png'))
        else:
            self.label.setPixmap(QPixmap('max.png'))"""

    
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QWidget, QSlider, QMainWindow, QPushButton, QLabel, QLineEdit, QInputDialog, QApplication, QDialog)
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time, telnetlib, re, threading


class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        while True:
            global rawMsg
            global levelFlag
            rawMsg = tn.read_very_eager()
            cookedMsg = re.search(b'! "publishToken":"(.*)" "value":(.*)\r\n',rawMsg)
            if levelFlag:
                try:
                    level = cookedMsg.group(2).decode("utf-8")
                    #print("REGEX is " + level)
                    level = float(level) + 100
                    levelFlag = False
                    sld.setValue(level)
                    levelFlag = True
                    time.sleep(0.3)
                except Exception as e:
                    n=1

class subsPause (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        global levelFlag
        levelFlag = False
        time.sleep(2)
        levelFlag = True


class Example(QWidget):


    def __init__(self):
        super().__init__()

        self.initUI()
        #self.connectTesira()


    def initUI(self):
        global sld
        
        sld = QSlider(Qt.Vertical,self)
        sld.setFocusPolicy(Qt.NoFocus)
        
        sld.setMaximum(100)
        sld.setMinimum(60)
        sld.setTickInterval(3)
        sld.setTickPosition(QSlider.TicksBothSides)


        self.btn = QtWidgets.QPushButton('IP address', self)
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
        sld.sliderPressed.connect(self.onSliderPress)
        sld.sliderReleased.connect(self.onSliderRelease)

        self.setGeometry(300, 300, 320, 300)
        self.setWindowTitle('biamp slider test')

        
        self.show()
        

    def connectTesira(self):
        global tn
        global InstanceTag
        tn = telnetlib.Telnet(HOST)
        tn.set_debuglevel(4)
        tn.read_until(b'...\r\n', timeout=10)
        print("telnet connected")
        subs = InstanceTag +" subscribe level 1 123\n"
        subs = subs.encode(encoding="utf-8")
        tn.write(subs)
        self.thread1 = myThread(1,"src-level")
        self.thread1.start()
        self.le.setText('connected')     
        

    def onSliderPress(self):
        global levelFlag
        #levelFlag = True
        

    def onSliderRelease(self):
        global levelFlag
        #levelFlag = False


    def changeValue(self, Svalue):

        Svalue = Svalue-100
        value = str(Svalue)
        s = InstanceTag + " set level " + level + " " + value + "\n"
        s = s.encode(encoding="utf-8")
        self.thread2 = subsPause(2,"src-Pause")
        self.thread2.start()
        tn.write(s)



    def showDialog(self):
        global HOST
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter IP address:')
        HOST = str(text)
        try:
            tn.close()
        except Exception as e:
                    n=1
        self.connectTesira()


    def showDialogIST(self):
        global InstanceTag
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter Instance Tag:')
        InstanceTag = str(text)
        try:
            tn.close()
        except Exception as e:
                    n=1
        self.connectTesira()
        



        
if __name__ == '__main__':

    HOST = "192.168.6.253"
    InstanceTag = 'Level13'
    level = str(1)
    value = str(0)
    levelFlag = True
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


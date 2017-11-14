from PyQt5.QtWidgets import (QWidget, QSlider, QMainWindow, QPushButton, QLabel, QLineEdit, QInputDialog, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import telnetlib


HOST = "192.168.6.253"
tn = telnetlib.Telnet(HOST)
subs = b"AudioMeter1 subscribe level 1 123 1000"
tn.set_debuglevel(5)
tn.read_until(b"Welcome to the Tesira Text Protocol Server...")
print("telnet connected")

#tn.write(subs)
tn.close()
try:
    tn.write(subs)
    
except Exception as e:
    
    tn = telnetlib.Telnet(HOST)
    tn.set_debuglevel(5)
    tn.read_until(b"Welcome to the Tesira Text Protocol Server...")

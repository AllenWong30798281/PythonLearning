import sys
import telnetlib
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


HOST = "192.168.6.253"
ls = "Level13 toggle mute 1\n"
ls = ls.encode(encoding="utf-8")
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Welcome to the Tesira Text Protocol Server...")




class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        btn1 = QPushButton("Mute", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Mute", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Telnet test')
        self.show()





    def buttonClicked(self):
        tn.write(ls)
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

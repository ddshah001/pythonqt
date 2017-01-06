import sys
from PyQt4 import QtGui, QtCore

class win(QtGui.QMainWindow):

    def __init__(self):
        super(win, self).__init__()
        self.setGeometry(50,100,500,300)
        self.setWindowTitle("Class Structur")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        eaexit = QtGui.QAction("&Exit",self)
        eaexit.setShortcut("Ctrl+E")
        eaexit.setStatusTip('Trying to exit')
        eaexit.triggered.connect(self.close_app)

        eachangetitle = QtGui.QAction("Change Title",self)
        eachangetitle.setShortcut("Ctrl+t")
        eachangetitle.setStatusTip("Title Changed")
        eachangetitle.triggered.connect(self.Change_title)

        self.statusBar()

        mm = self.menuBar()
        fm = mm.addMenu('&File')
        fm.addAction(eaexit)

        fm.addAction(eachangetitle)


        self.homescreen()

    btnaligny = 200
    text = ""


    def homescreen(self):
        self.setWindowTitle("Home Login")
        btn = QtGui.QPushButton("Close Direct", self)
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.resize(100,50)
        btn.move(100,self.btnaligny)

        btn2 =QtGui.QPushButton("Close Function", self)
        btn2.clicked.connect(self.close_app)
        btn2.resize(btn2.sizeHint())
        btn2.move(200,self.btnaligny)

        btn3 = QtGui.QPushButton("Change Title", self)
        btn3.clicked.connect(self.Change_title)
        btn3.resize(80, 40)
        btn3.move(300, self.btnaligny)

        self.textbox = QtGui.QLineEdit(self)
        self.textbox.move(100,150)
        self.textbox.resize(self.textbox.sizeHint())

        checkbox = QtGui.QCheckBox('Change Title',self)
        checkbox.move(250,145)
        checkbox.stateChanged.connect(self.large)




        mm = self.menuBar()
        em = mm.addMenu("&Edit")

        eat = QtGui.QAction(QtGui.QIcon('logo-php.png'),'PHP',self)
        eat.triggered.connect(self.close_app)

        ejt = QtGui.QAction(QtGui.QIcon("java-logo.png"),"JAVA",self)
        #ejt.triggered.connect(self.close_app)

        self.toolBar = self.addToolBar("PHP")
        self.toolBar.addAction(eat)
        self.toolBar.addAction(ejt)

        self.show()

    def large(self, s):
        if s == QtCore.Qt.Checked:
            self.setWindowTitle(self.textbox.text())

        else:
            self.setWindowTitle("Class Structur")

    def close_app(self):
        choice = QtGui.QMessageBox.question(self, "Close", "Want to exit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass




    def Change_title(self):
        self.setWindowTitle("Title Changed")


app = QtGui.QApplication(sys.argv)
G = win()
sys.exit(app.exec_())
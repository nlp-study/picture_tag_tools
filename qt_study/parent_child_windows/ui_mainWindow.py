from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.xianjian_widget = QtWidgets.QWidget(self.centralwidget)
        self.xianjian_widget.setGeometry(QtCore.QRect(0, 0, 300, 200))
        self.xianjian_widget.setObjectName("xianjian_widget")
        self.label = QtWidgets.QLabel(self.xianjian_widget)
        self.label.setGeometry(QtCore.QRect(70, 70, 91, 16))
        self.label.setObjectName("label")

        self.qixia_widget = QtWidgets.QWidget(self.centralwidget)
        self.qixia_widget.setGeometry(QtCore.QRect(0, 0, 300, 200))
        self.qixia_widget.setObjectName("qixia_widget")
        self.label_2 = QtWidgets.QLabel(self.qixia_widget)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 54, 12))
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionXian = QtWidgets.QAction(MainWindow)
        self.actionXian.setObjectName("actionXian")
        self.actionQi = QtWidgets.QAction(MainWindow)
        self.actionQi.setObjectName("actionQi")
        self.menu.addAction(self.actionXian)
        self.menu.addAction(self.actionQi)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "仙剑窗口"))
        self.label_2.setText(_translate("MainWindow", "奇侠窗口"))
        self.menu.setTitle(_translate("MainWindow", "仙剑奇侠"))
        self.actionXian.setText(_translate("MainWindow", "Xian"))
        self.actionQi.setText(_translate("MainWindow", "Qi"))


from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, Qt, QPoint
from PyQt5.QtGui import QMouseEvent

import sys,os


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        # 首先隐藏所有widget
        self.xianjian_widget.hide()
        self.qixia_widget.hide()
        self.actionXian.triggered.connect(self.openXianjian)
        self.actionQi.triggered.connect(self.openQixia)

    def openXianjian(self):
        self.qixia_widget.hide()
        self.xianjian_widget.show()

    def openQixia(self):
        self.xianjian_widget.hide()
        self.qixia_widget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main = Main()
    Main.show()
    sys.exit(app.exec_())
    pass

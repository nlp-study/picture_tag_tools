'''
标注2.0版，目前要处理的是一张图片一个标签，点击按钮就能直接保存
'''

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 40, 171, 41))
        self.label.setStyleSheet("color: rgb(170, 85, 255);\nfont: 14pt \"楷体\";")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "qt designer 窗口"))


# 主函数代码（基本通用）

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()  #类名
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

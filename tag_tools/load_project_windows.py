from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class LoadProjectWidget(QWidget):
    def __int__(self):
        self.setObjectName("Form2")
        self.resize(400, 300)
        self.load_image_folder_bt = QtWidgets.QPushButton(self)
        self.load_image_folder_bt.setGeometry(QtCore.QRect(0, 0, 54, 54))
        self.load_image_folder_bt.setObjectName("打开图片文件夹")
        self.load_image_folder_bt.text("打开图片文件夹")
        self.load_image_folder_bt.clicked.connect(self.openFolder)

        self.load_tag_result_bt = QtWidgets.QPushButton(self)
        self.load_tag_result_bt.setGeometry(QtCore.QRect(320, 270, 75, 23))
        self.load_tag_result_bt.setObjectName("打开标注结果文件夹")

        # self.retranslateUi(self)
        # QtCore.QMetaObject.connectSlotsByName(self)



    def openFolder(self):
        '''
        加载须标注文件夹
        :return:
        '''
        directory = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        print("directory:", directory)
        self.get_all_image_path(directory)
        print("self.current_image_list size", len(self.current_image_list))
        self.processing_image_name = self.current_image_list[-1]


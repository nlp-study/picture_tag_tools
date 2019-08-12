import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from tools.file_operation import *
from tools.list_operation import *
from tag_tools.load_project import *

# class loadProjectWidget(QWidget,Ui_Form2):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)  # 初始化运行B窗口类下的 setupUi 函数
#         self.B_bt1.clicked.connect(self.close) #窗口2 中的关闭按钮

class tagPicture(QMainWindow):
    def __init__(self):
        super(tagPicture, self).__init__()
        self.label_list = ["porn","sexy"]
        self.candidate_image_list = []
        self.processed_image_list = []
        self.current_image_list = []
        self.processing_image_name = ""
        self.tag_output_folder = "I:\github_nsfw_tags"

        self.resize(1200, 800)
        self.setWindowTitle("label显示图片")

        self.label = QLabel(self)
        self.label.setText("显示图片")
        self.label.setFixedSize(800, 800)
        self.label.move(160, 160)
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}")
        # btn = QPushButton(self)
        # btn.setText("打开图片")
        # btn.move(10, 30)
        # btn.clicked.connect(self.openFolder)

        self.build_tools()
        self.build_label_btn()
        self.load_project()
        self.openXianjian()

    def build_tools(self):


        open_images_folder = QAction(QIcon('open.png'), 'Open', self)
        open_images_folder.setShortcut('Ctrl+O')
        open_images_folder.setStatusTip('Open new File')
        open_images_folder.triggered.connect(self.openFolder)

        iamge_menubar = self.menuBar()
        fileMenu = iamge_menubar.addMenu("加载图片文件夹")
        fileMenu.addAction(open_images_folder)


        tag_file_folder = QAction(QIcon('open.png'), 'Open', self)
        tag_file_folder.setShortcut('Ctrl+O')
        tag_file_folder.setStatusTip('Open new File')
        tag_file_folder.triggered.connect(self.open_tag_folder)
        tag_menubar = self.menuBar()
        tag_file_menu = tag_menubar.addMenu("加载输出文件夹")
        tag_file_menu.addAction(tag_file_folder)

    def load_project(self):
        self.xianjian_widget = QtWidgets.QWidget(self)
        self.xianjian_widget.setGeometry(QtCore.QRect(0, 0, 300, 200))
        self.xianjian_widget.setObjectName("xianjian_widget")
        self.label = QtWidgets.QLabel(self.xianjian_widget)
        self.label.setGeometry(QtCore.QRect(70, 70, 91, 16))
        self.label.setObjectName("label")
        self.xianjian_widget.hide()

    def openXianjian(self):
        self.xianjian_widget.show()


    def build_label_btn(self):
        # for i in range(len(self.label_list)):
        #     tag_name = self.label_list[i]
        #     btn_y = 30 * (i + 2)
        #     temp_btn = QPushButton(self)
        #     temp_btn.setText(tag_name)
        #     temp_btn.move(10, btn_y)
        #     temp_btn.clicked.connect(lambda: self.label_image(self.label_list[i]))
        button1 = QPushButton(self)
        button1.setText(self.label_list[0])
        btn_y = 60
        button1.move(10, btn_y)
        button1.clicked.connect(lambda: self.tag_image(self.label_list[0]))
        button2 = QPushButton(self)
        button2.setText(self.label_list[1])
        btn_y += 30
        button2.move(10, btn_y)
        button2.clicked.connect(lambda: self.tag_image(self.label_list[1]))


        # for i in range(len(self.tag_btn_list)):
        #     tag_name = self.label_list[i]
        #     btn_y = 30*(i+2)
        #     temp_btn = QPushButton(self)
        #     temp_btn.setText(tag_name)
        #     temp_btn.move(10, btn_y)
        #     temp_btn.clicked.connect(lambda:self.label_image(self.label_list[i]))


    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        print("imgName:",imgName)
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

    def tag_image(self,tag_name):
        print("tag_name:",tag_name)
        line = "<image_path>" + self.processing_image_name + "</image_path>\r\n" + "<tag_name>" + tag_name + "</tag_name>"
        image_name = os.path.basename(self.processing_image_name)
        image_suf = image_name.split(".")[-1]
        image_tag_name = image_name.replace("."+image_suf,".txt")
        output_path = self.get_tag_file_name(self.tag_output_folder,image_tag_name)
        write_one_line(line,output_path)

        self.processed_image_list.append(self.processing_image_name)
        self.current_image_list.pop()
        self.processing_image_name = self.current_image_list[-1]
        self.show_image()


    def openFolder(self):
        '''
        加载须标注文件夹
        :return:
        '''
        directory = QFileDialog.getExistingDirectory(self,   "选取文件夹",   "./")
        print("directory:",directory)
        self.get_all_image_path(directory)
        print("self.current_image_list size",len(self.current_image_list))
        self.processing_image_name = self.current_image_list[-1]
        self.show_image()


    def open_tag_folder(self):
        '''
        重定向标注文件
        :return:
        '''
        directory = QFileDialog.getExistingDirectory(self,   "选取文件夹",   "./")
        self.tag_output_folder = directory
        print("tag_output_folder:", self.tag_output_folder)

    def get_all_image_path(self,input_folder):
        '''
        加载须标注文件夹的时候，找到下面所有的图片
        :param input_folder:
        :return:
        '''
        self.candidate_image_list = []
        get_all_images(input_folder, self.candidate_image_list)
        self.current_image_list = list(set(self.candidate_image_list) - set(self.processed_image_list))
        self.current_image_list.sort()


    def show_image(self):
        print("show image:",self.processing_image_name)
        image = QtGui.QPixmap(self.processing_image_name).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(image)

    def get_tag_file_name(self,result_folder,result_name):
        '''
        处理标注文件重名的问题
        :param result_folder:
        :param result_name:
        :return:
        '''
        result_path = result_folder + os.sep + result_name
        iter_number = 1
        while os.path.exists(result_path):
            result_path = result_folder + os.sep + str(iter_number) + "_" + result_name
        return result_path


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = tagPicture()
    my.show()
    sys.exit(app.exec_())

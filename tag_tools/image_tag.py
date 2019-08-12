import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from tools.file_operation import *
from tools.list_operation import *
from tag_tools.process_tag_file import *

class LoadPojectDialog(QDialog):
    def __init__(self, parent=None):
        super(LoadPojectDialog, self).__init__(parent)
        self.resize(550, 300)
        self.input_image_folder = ""
        self.tag_output_folder = "I:\\github_nsfw_tags\\formal"

        # layout = QVBoxLayout(self)
        btn_x = 10
        btn_y = 60
        self.button1 = QPushButton(self)
        self.button1.setText("加载文件夹")

        self.button1.move(btn_x, btn_y)
        self.button1.clicked.connect(self.open_image_folder)
        self.image_folder_label = QLabel(self)
        self.image_folder_label.resize(300,40)
        self.image_folder_label.move(130, btn_y)
        self.image_folder_label.setWordWrap(True)

        self.button2 = QPushButton(self)
        self.button2.setText("加载输出目录")
        btn_y += 60
        self.button2.move(btn_x, btn_y)
        self.button2.clicked.connect(self.open_tag_output_folder)
        self.tag_result_label = QLabel(self)
        self.tag_result_label.resize(300, 40)
        self.tag_result_label.move(130, btn_y)
        self.tag_result_label.setWordWrap(True)
        self.tag_result_label.setText(self.tag_output_folder)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)  # 点击ok，隐士存在该方法
        buttons.rejected.connect(self.reject)  # 点击cancel，该方法默认隐士存在
        btn_y += 60
        buttons.move(btn_x,btn_y)
        # layout.addWidget(buttons)
        self.show()

    def open_image_folder(self):
        '''
        加载须标注文件夹
        :return:
        '''
        self.input_image_folder = QFileDialog.getExistingDirectory(self,   "选取文件夹",   "./")
        print("self.input_image_folder:",self.input_image_folder)
        self.image_folder_label.setText(self.input_image_folder)

    def open_tag_output_folder(self):
        '''
        打开加载标注结果的文件夹
        :return:
        '''
        self.tag_output_folder = QFileDialog.getExistingDirectory(self,   "选取文件夹",   self.tag_output_folder)
        print("self.input_image_folder:",self.input_image_folder)
        self.tag_result_label.setText(self.tag_output_folder)

class tagPicture(QMainWindow):
    def __init__(self):
        super(tagPicture, self).__init__()
        self.label_list = ["porn","cartoon_porn","sexy","cartoon_sexy","delete","other"]
        self.special_label_list = ["good"]
        self.candidate_image_list = []
        self.processed_image_list = []
        self.current_image_list = []
        self.processing_image_name = ""
        self.input_image_folder = ""
        self.tag_output_folder = ""

        self.resize(1200, 800)
        self.setWindowTitle("label显示图片")

        self.label = QLabel(self)
        self.label.setText("显示图片")
        self.label.setFixedSize(800, 800)
        self.label.move(70, 70)
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}")

        self.show_processing_image()
        self.open_project()
        self.build_label_btn()
        # self.openXianjian()


    def show_processing_image(self):
        button1 = QPushButton(self)
        button1.setText("打开文件所在文件夹")
        button1.resize(140,30)
        button1.move(10, 30)
        button1.clicked.connect(self.open_image_folder)


        self.image_path_label = QLabel(self)
        self.image_path_label.setText("显示图片地址")
        self.image_path_label.setFixedSize(800, 40)
        self.image_path_label.move(190, 20)
        self.image_path_label.setTextInteractionFlags(Qt.TextSelectableByMouse)#

    def open_image_folder(self):
        '''
        打开正在处理的图片所在的文件夹
        :return:
        '''
        if self.processing_image_name is None or len(self.processing_image_name) ==0:
            return
        current_folder = os.path.split(self.processing_image_name)
        print("current_folder:", current_folder)
        standard_path = os.path.abspath(current_folder[0])
        os.system("start explorer " + standard_path)


    def open_project(self):
        '''
        加载项目
        :return:
        '''
        open_images_folder = QAction(QIcon('open.png'), 'Open', self)
        open_images_folder.setShortcut('Ctrl+O')
        open_images_folder.setStatusTip('Open new File')
        # open_images_folder.triggered.connect(self.openFolder)
        open_images_folder.triggered.connect(self.load_project)
        iamge_menubar = self.menuBar()

        fileMenu = iamge_menubar.addMenu("加载图片文件夹")
        fileMenu.addAction(open_images_folder)


    def load_project(self):
        dialog=LoadPojectDialog()
        res=dialog.exec_()
        self.input_image_folder = dialog.input_image_folder
        self.tag_output_folder = dialog.tag_output_folder
        print("self.input_image_folder:", self.input_image_folder)
        print("self.tag_output_folder:", self.tag_output_folder)

        if self.input_image_folder is None or len(self.input_image_folder) ==0 :
            print("input_image_folder is empty!")
            return
        if self.tag_output_folder is None or len(self.tag_output_folder) ==0 :
            print("tag_output_folder is empty!")
            return
        processed_image_set = parse_tag_file_by_folder(self.tag_output_folder)
        self.processed_image_list = list(processed_image_set)
        self.processed_image_list.sort()
        self.get_all_image_path(self.input_image_folder)

        print("self.current_image_list size", len(self.current_image_list))
        print("self.processed_image_list size", len(self.processed_image_list))

        if len(self.current_image_list) == 0:
            self.processing_image_name = ""
            print("proces list empty!")
            reply = QMessageBox.information(self, '标题', '图片已经处理完毕', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        self.processing_image_name = self.current_image_list[-1]
        self.show_image()

    def get_all_image_path(self,input_folder):
        '''
        加载须标注文件夹的时候，找到下面所有的图片
        :param input_folder:
        :return:
        '''
        self.candidate_image_list = []
        get_all_images(input_folder, self.candidate_image_list)
        if len(self.candidate_image_list) == 0:
            reply = QMessageBox.information(self, '标题', input_folder+'下图片为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        self.current_image_list = list(set(self.candidate_image_list) - set(self.processed_image_list))
        self.current_image_list.sort()


    def build_label_btn(self):
        btn_x = 900
        #标注按钮
        button1 = QPushButton(self)
        button1.setText(self.label_list[0])
        btn_y = 60
        button1.move(btn_x, btn_y)
        button1.clicked.connect(lambda: self.tag_image(self.label_list[0]))
        button1.setStyleSheet("background-color:rgb(255,0,0)")

        button2 = QPushButton(self)
        button2.setText(self.label_list[1])
        button2.move(btn_x + 120, btn_y)
        button2.clicked.connect(lambda: self.tag_image(self.label_list[1]))
        button2.setStyleSheet("background-color:rgb(255,0,0)")

        button3 = QPushButton(self)
        button3.setText(self.label_list[2])
        btn_y += 40
        button3.move(btn_x, btn_y)
        button3.clicked.connect(lambda: self.tag_image(self.label_list[2]))
        button3.setStyleSheet("background-color:rgb(255,20,147)")

        button4 = QPushButton(self)
        button4.setText(self.label_list[3])
        button4.move(btn_x + 120, btn_y)
        button4.clicked.connect(lambda: self.tag_image(self.label_list[3]))
        button4.setStyleSheet("background-color:rgb(255,20,147)")

        button5 = QPushButton(self)
        button5.setText(self.label_list[4])
        btn_y += 40
        button5.move(btn_x, btn_y)
        button5.clicked.connect(lambda: self.tag_image(self.label_list[4]))
        button5.setStyleSheet("background-color:rgb(0,103,9)")

        button6 = QPushButton(self)
        button6.setText(self.label_list[5])
        btn_y += 40
        button6.move(btn_x, btn_y)
        button6.clicked.connect(lambda: self.tag_image(self.label_list[5]))
        button6.setStyleSheet("background-color:rgb(100,103,9)")

        #特殊标注按钮，只标注，不直接next
        special_button1 = QPushButton(self)
        special_button1.setText(self.special_label_list[0])
        btn_y += 60
        special_button1.move(btn_x, btn_y)
        special_button1.clicked.connect(lambda: self.special_tag_image(self.special_label_list[0]))
        special_button1.setStyleSheet("background-color:rgb(200,103,9)")

        #上一张图片，下一张图片
        pre_button = QPushButton(self)
        pre_button.setText('pre image')
        btn_y += 160
        pre_button.move(btn_x, btn_y)
        pre_button.clicked.connect(self.get_pre_image)
        pre_button.setStyleSheet("background-color:rgb(200,103,9)")

        next_button = QPushButton(self)
        next_button.setText('next image')
        btn_y += 60
        next_button.move(btn_x, btn_y)
        next_button.clicked.connect(self.get_next_image)
        next_button.setStyleSheet("background-color:rgb(200,103,9)")

    def tag_image(self, tag_name):
        '''
        打上标记，而且自动运行到下一个
        :param tag_name:
        :return:
        '''
        if self.processing_image_name is None or len(self.processing_image_name) == 0:
            print("no image left")
            reply = QMessageBox.information(self, '标题', '图片已经处理完毕', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        print("tag_name:", tag_name)
        line = "<tag_image><image_path>" + self.processing_image_name + "</image_path>\r\n" + "<tag_name>" + tag_name + "</tag_name></tag_image>"
        image_name = os.path.basename(self.processing_image_name)
        image_suf = image_name.split(".")[-1]
        image_tag_name = image_name.replace("." + image_suf, ".txt")
        output_path = self.get_tag_file_name(self.tag_output_folder, image_tag_name)
        write_one_line(line, output_path)

        self.processed_image_list.append(self.processing_image_name)
        self.processing_image_name = self.current_image_list.pop()
        self.show_image()

    def special_tag_image(self, tag_name):
        '''
        打上标记，但是不会自动运行到下一个
        :param tag_name:
        :return:
        '''
        if self.processing_image_name is None or len(self.processing_image_name) == 0:
            print("no image left")
            reply = QMessageBox.information(self, '标题', '图片已经处理完毕', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        print("tag_name:", tag_name)
        line = "<special_tag_image><image_path>" + self.processing_image_name + "</image_path>\r\n" + "<tag_name>" + tag_name + "</tag_name></special_tag_image>"
        image_name = os.path.basename(self.processing_image_name)
        image_suf = image_name.split(".")[-1]
        image_tag_name = image_name.replace("." + image_suf, ".txt")
        output_path = self.get_tag_file_name(self.tag_output_folder, image_tag_name)
        write_one_line(line, output_path)



    def show_image(self):
        if self.processing_image_name is None or len(self.processing_image_name) == 0:
            print("processing_image_name is empty")
            reply = QMessageBox.information(self, '标题', '图片已经处理完毕', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        print("show image:",self.processing_image_name)
        image = QtGui.QPixmap(self.processing_image_name).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(image)
        self.image_path_label.setText(self.processing_image_name)

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
            iter_number +=1
        return result_path


    def get_pre_image(self):
        '''
        展示前面一张图片
        :return:
        '''
        if len(self.processed_image_list) == 0:
            reply = QMessageBox.information(self, '标题', '这是第一张图片，前面没有处理过的图片', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        if self.processing_image_name is not None and len(self.processing_image_name) !=0:
            self.current_image_list.append(self.processing_image_name)
        self.processing_image_name = self.processed_image_list.pop()
        self.show_image()

    def get_next_image(self):
        '''
        展示后面一张图片
        :return:
        '''
        if len(self.current_image_list) == 0:
            reply = QMessageBox.information(self, '标题', '图片已经处理完成', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        if self.processing_image_name is not None and len(self.processing_image_name) !=0:
            self.processed_image_list.append(self.processing_image_name)
        self.processing_image_name = self.current_image_list.pop()
        self.show_image()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = tagPicture()
    my.show()
    sys.exit(app.exec_())

#coding=utf-8
#按钮操作
 
import sys
import os
import shutil 
from PyQt4.QtGui import *  
from PyQt4.QtCore import * 
WINDOW_WIDTH = 1200
WINDOW_HIGHT = 1000
IMAGE_HIGHT = 850
FILE_TYPE = ['jpg', 'jpeg', 'tif', 'bmp']

class Window( QWidget ):
    def __init__( self,pic_root,god_folder,bad_folder,other_folder):
        super( Window, self ).__init__()
        self.pic_root = pic_root
        self.god_folder = god_folder
        self.bad_folder = bad_folder
        self.other_folder = other_folder
        self.folder_list = [] 
        self.current_pic_file = ""

        self.setWindowTitle( "hello" )
        self.resize( WINDOW_WIDTH, WINDOW_HIGHT )
        self.gridlayout = QGridLayout()
         
        self.button1 = QPushButton( "好图片" )
        self.button1.setFixedSize(QSize(110,130))
        self.button1.clicked.connect(self._set_god_pic) 

        
         
        self.button2 = QPushButton( "不好的图片" )
        self.button2.setFixedSize(QSize(110,130))
        self.button2.clicked.connect(self._set_bad_pic) 
        
        self.gridlayout.addWidget( self.button1, 0, 20, 1, -1 )
        self.gridlayout.addWidget( self.button2, 2, 20, 1, -1 )

        self.setWindowTitle(self.tr("Picture Tag tools 1.0"))  
        self.imageLabel=QLabel() 

        self._build_folder_list()
        self.current_pic_file = self._find_pic()
        print("self.current_pic_file: ",self.current_pic_file)
        self._load_pic(self.current_pic_file)
        self.setLayout( self.gridlayout)

    def _load_pic(self,pic_name):
        print ("_load_pic: ",pic_name)
        self.imageLabel.clear()
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)  
        # self.setCentralWidget(self.imageLabel)  
        self.image = QImage()  
  
        if self.image.load(pic_name):  
            size = self.image.size()
            width = WINDOW_HIGHT - 10
            size.scale(width, width, Qt.KeepAspectRatio)
            print("size",size.width())
            self.imageLabel.setPixmap(QPixmap.fromImage(self.image.scaled(size)))
            self.gridlayout.addWidget(self.imageLabel,0, 0,20,20)

    def _set_god_pic(self):
        if(self.current_pic_file == ""):
            print("no more picture in root_file")
            return
        self._move_file(self.current_pic_file, self.god_folder)
        print("old picture: ",self.current_pic_file," is a good pic!")
        self.current_pic_file = self._find_pic()
        self._load_pic(self.current_pic_file)
        print("new picture: ",self.current_pic_file)


    def _set_bad_pic(self):
        print("it is a bad pic!")
        if(self.current_pic_file == ""):
            print("no more picture in root_file")
            return
        self._move_file(self.current_pic_file, self.bad_folder)
        print("old picture: ",self.current_pic_file," is a good pic!")
        self.current_pic_file = self._find_pic()
        self._load_pic(self.current_pic_file)
        print("new picture: ",self.current_pic_file)


    def _find_pic(self):
        self._find_folder()
        current_foler = self.folder_list[-1]
        files = os.listdir(current_foler)
        pic_name = ""

        for file in files:
            suffex = file.split('.')[-1]
            print("suffex: ",suffex)
            pic_name = current_foler + os.sep + file
            if  suffex in FILE_TYPE:
                return pic_name
            else: 
                self._move_file(pic_name, self.other_folder)
        
        return "";

    def _find_folder(self):
        current_folder = self.folder_list[-1]
        while not self._check_exist_pics(current_folder):
            if current_folder == self.pic_root:
                print("picture all processed!")
                exit()
                return
            shutil.rmtree(current_folder)
            self._build_folder_list()
            current_folder = self.folder_list[-1]


    def _check_exist_pics(self,current_folder):
        files = os.listdir(current_folder)
        if(len(files) == 0):
            print("current_folder: ",current_folder," no files")
            return False

        for file in files:
            suffex = file.split('.')[-1]
            if  suffex in FILE_TYPE:
                return True
        
        return False


    def _move_file(self,src_file,dist_folder):
        temp_file = os.path.basename(src_file)
        sub_file = dist_folder + os.sep + temp_file
        if(os.path.exists(sub_file)):
            print(temp_file," exist at: ",sub_file," delelte it")
            os.remove(src_file)
        else:
            shutil.move(src_file, dist_folder)




    def _build_folder_list(self):
        is_exist_next_foler = True
        self.folder_list = []
        self.folder_list.append(self.pic_root)
        while(is_exist_next_foler):
            is_exist_foler = False
            current_foler = self.folder_list[-1]
            folers = os.listdir(current_foler)
            # print '\n'.join(folers)
            for temp_foler in folers:
                sub_folder = current_foler + os.sep + temp_foler
                if(os.path.isdir(sub_folder)):
                    is_exist_foler = True
                    self.folder_list.append(sub_folder)
                    break;
            if(not is_exist_foler):
                break;
        print("folder line:",self.folder_list)





def main(argv):
    print('\n'.join(argv))
    pic_root = "F:/pic/test/finish_copy"
    god_folder = "F:/pic/pic_classification/pic_good"
    bad_folder = "F:/pic/pic_classification/pic_bad"
    other_folder = "F:/pic/pic_classification/other_file"
    app=QApplication(sys.argv)  
    main=Window(pic_root,god_folder,bad_folder,other_folder)  
    main.show()  
    app.exec_()  

if __name__ == '__main__':
    main(sys.argv)


'''
Created on 2016年6月21日

@author: Zhang Xiulong
'''
import shutil 
import os

def copy_file(source_file,target_file):
    if not os.path.exists(source_file):
        print('copy file failure,source file is not exist!')
    shutil.copy(source_file,  target_file)


def get_all_files(path,file_list):
    allfilelist=os.listdir(path)
    # 遍历该文件夹下的所有目录或者文件
    for file in allfilelist:
        filepath = path + os.sep + file
        # 如果是文件夹，递归调用函数
        if os.path.isdir(filepath):
            get_all_files(filepath,file_list)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(filepath):
            file_list.append(filepath)


image_suf_list = ['bmp','jpg','png','BMP','JPG','PNG','JPEG','jpeg']
# image_suf_list= []
def get_all_images(input_folder,file_list):

    all_file_list = os.listdir(input_folder)
    for file in all_file_list:
        file_path = input_folder + os.sep + file
        # 如果是文件夹，递归调用函数
        if os.path.isdir(file_path):
            get_all_images(file_path, file_list)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(file_path):
            file_suf = file_path.split(".")[-1]
            if file_suf in image_suf_list:
                # if file_suf == "ini":
                file_list.append(file_path)



     
if __name__ == '__main__':
    source_file = 'd:/test.txt'
    target_file = 'd:/test_1.txt'
    # copy_file(source_file,target_file)

    folder_path = "C:/Users/Administrator/Pictures"
    file_list = []
    get_all_images(folder_path, file_list)
    print("file_list :",file_list)
    print("file_list size:", len(file_list))
    file_list = list(set(file_list))
    print("file_list size:", len(file_list))
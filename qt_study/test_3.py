import os

path = os.getcwd()
path = "C:\\Users\\Administrator\\Pictures\\截图\\捕获3.PNG"
path = "C:/Users/Administrator/Pictures/截图/捕获3.PNG"
current_folder = os.path.split(path)
print("current_folder:",current_folder)
folder_path = current_folder[0]
standard_path = os.path.abspath(folder_path)
print("standard_path:",standard_path)
os.system('explorer.exe /n, '+ standard_path)
# os.system("start explorer " + current_folder[0])
# os.system("start explorer " + current_folder[0])
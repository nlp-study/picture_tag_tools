from xml.etree import ElementTree as ET

from tools.file_operation import *
from tools.list_operation import *

def parse_tag_file_by_folder(input_folder):
    xml_file_list = os.listdir(input_folder)
    image_path_set = set()
    for xml_file in xml_file_list:
        xml_path = input_folder + os.sep + xml_file
        if not os.path.isfile(xml_path):
            continue
        image_path, tag_name = parse_tag_file(xml_path)
        if len(image_path) == 0:
            continue
        image_path_set.add(image_path)
    return image_path_set




def parse_tag_file(input_file):
    xml_text = read_text(input_file)
    print("xml_text:",xml_text)
    root = ET.XML(xml_text)

    image_path = ""
    tag_name = ""
    print("root:",root)
    for obj in root.iter('image_path'):
        print("obj:",obj)
        print("text:",obj.text)
        image_path = obj.text
    for obj in root.iter("tag_name"):
        tag_name = obj.text
    return image_path, tag_name


if __name__ == "__main__":
    input_file = "I:\github_nsfw_tags\李荣福.txt"
    image_path, tag_name = parse_tag_file(input_file)
    print("image_path:",image_path)
    print("tag_name:",tag_name)

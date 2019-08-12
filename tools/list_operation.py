'''
Created on 2016年5月3日

@author: Administrator
'''
import codecs
import os

def read_list(input_file):
    if input_file == None:
        return []
    read_result = []
    read_file = codecs.open(input_file,'r','utf-8')
    for line in read_file:
        line = line.strip()
        if line == '':
            continue
        read_result.append(line)
    return read_result

def read_text(input_file):
    if input_file == None:
        return []
    read_result = ""
    read_file = codecs.open(input_file,'r','utf-8')
    for line in read_file:
        line = line.strip()
        if line == '':
            continue
        read_result += line
    return read_result

def read_list_from_folder(input_folder):
    files = os.listdir(input_folder)
    read_result = []
    for file in files:
        sub_file = input_folder + os.sep + file
        temp_list = read_list(sub_file)
        read_result += temp_list
    return read_result
    
def write_list(input_list,output_path):
    write_file = codecs.open(output_path,'w','utf-8')
    for line in input_list:
        write_file.write(str(line) + '\n')
    write_file.close()

def write_add_one_line(line,output_path):
    write_file = codecs.open(output_path,'a+','utf-8')
    write_file.write(str(line) + '\n')
    write_file.close()

def write_one_line(line,output_path):
    write_file = codecs.open(output_path,'w','utf-8')
    write_file.write(str(line) + '\n')
    write_file.close()
    
def write_str_map(input_map,output_path):
    write_file = codecs.open(output_path,'w','utf-8')
    for key in input_map:
        value = input_map[key]
        write_str = key + '\t' + str(value) + '\n'
        write_file.write(write_str)
    write_file.close()
    
def write_str_int_map(input_map,output_path):
    write_file = codecs.open(output_path,'w','utf-8')
    for key in input_map:
        value = input_map[key]
        write_str = key + '\t' + str(value) + '\n'
        write_file.write(write_str)
    write_file.close()
    
def write_sorted_str_int_map(input_map,output_path):
    dict= sorted(input_map.items(), key=lambda d:d[1], reverse = True)
    write_file = codecs.open(output_path,'w','utf-8')
    for temp_item in dict:
        key = temp_item[0]
        value = temp_item[1]
        write_str = key + '\t' + str(value) + '\n'
        write_file.write(write_str)
    write_file.close()
    
    
def write_sorted_str_int_map_ascending_order(input_map,output_path):
    dict= sorted(input_map.items(), key=lambda d:d[1], reverse = False)
    write_file = codecs.open(output_path,'w','utf-8')
    for temp_item in dict:
        key = temp_item[0]
        value = temp_item[1]
        write_str = key + '\t' + str(value) + '\n'
        write_file.write(write_str)
    write_file.close()
    
    
def write_list_list(input_list,output_path):
    write_file = codecs.open(output_path,'w','utf-8')
    for line_list in input_list:
        for term  in line_list:
            write_file.write(str(term) + '\t')
        write_file.write('\n')
    write_file.close()
    
if __name__ == '__main__':
    input_map = {'key1':1,'key2':2}
    output_path = '../../result_data/temp.txt'
    write_sorted_str_int_map(input_map,output_path)
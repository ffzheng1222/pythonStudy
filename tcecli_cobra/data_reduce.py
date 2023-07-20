# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : data_reduce.py
# Time       ：2022/4/10 00:00
# Author     ：p_fazheng
# version    ：python 3.8
# Description：
"""

import datetime
import yaml
import qsli_tool
import base64
import os
from pathlib import Path


# 保存文件的绝对路径以及其文件名
file_absolute_path_list = []


# 编码
def en_code(command_content):
    encodestr = base64.b64encode(command_content.encode(encoding='utf-8'))
    # 存入db的command_content
    return encodestr.decode()



# 读取本地已存在scripts目录下所有文件
def get_all_files(path):
    all_file_list = os.listdir(path)
    # 遍历该文件夹下的所有目录或文件
    for file in all_file_list:
        file_path = os.path.join(path, file)
        # 如果是文件夹，递归调用当前函数
        if os.path.isdir(file_path):
            get_all_files(file_path)
        # 如果不是文件夹，保存文件路径及文件名
        elif os.path.isfile(file_path):
            file_absolute_path_list.append(file_path)
    return file_absolute_path_list


#从scripts目录下的所有文件中过滤出manifest.yaml
def get_all_manifest(file_list):
    manifest_filestr = "manifest.yaml"
    all_manifest_filelist = []
    for fname in file_list:
        if str(fname).find(manifest_filestr) > 0:
            all_manifest_filelist.append(fname)
    return all_manifest_filelist


# 切割文件路径结构到对应的dir_struct_dict
def split_filename_str_to_dir_struct_dict(src_filename_str, dir_struct_keys, dir_struct_dict):
    #反转dir_struct_keys列表
    reversedlist_dir_struct_keys = list(reversed(dir_struct_keys))
    for key in reversedlist_dir_struct_keys:
        if len(os.path.split(src_filename_str)) == 2:
            dir_struct_dict[key] = os.path.split(src_filename_str)[1]
            src_filename_str = os.path.split(src_filename_str)[0]


# 分析scripts file文件目录结构
def analyze_scripts_file_dir_struct(scripts_path, odd_file_path):
    #  利用目录结构构件此dict
    #  {"cloud":"tce", "category":"common", "product":"tcenter", "component":"product-tcenter-support-ces", "scripts_file": "manifest.yaml"}
    dir_struct_dict = dict()
    dir_struct_keys = ["cloud", "category", "product", "component", "scripts_file"]

    src_filename_str = odd_file_path.replace(scripts_path, "", -1)
    # 将scripts文件目录结构拆解到dir_struct_dict字典中存储
    split_filename_str_to_dir_struct_dict(src_filename_str, dir_struct_keys, dir_struct_dict)
    return dir_struct_dict


# 解析manitest文件内容
def parse_manifest_content(data_record_dict, checkpoint_name, manifest_info):
    checkpoint_name_dict = dict(manifest_info['checkpoints'][checkpoint_name].items())
    # print(checkpoint_name_dict)
    data_record_dict['hosttype'] = checkpoint_name_dict['hosttype'] # hosttype 取值
    # severity 取值
    # severity = checkpoint_name_dict['severity']
    # 针对tcs 未改造部分 进行判断 if 'severity' not in checkpoint_name_dict:判断较慢，直接默认赋值
    data_record_dict['severity'] = 'high'

    description_old = checkpoint_name_dict['description']
    data_record_dict['description'] = description_old.replace("\"", "\'")   # description 取值

    # 清洗规则 str.replace 方法
    tag_old = checkpoint_name_dict['tag']
    data_record_dict['tag'] = str(tag_old).replace("\'", "")    # tag取值

    # command_type取值  command_code取值
    command = checkpoint_name_dict['command']
    if len(command) == 2:
        data_record_dict['command_type'] = command[0]
        # print(command[1])
        data_record_dict['command_code'] = command[1]


# 解析conmand 脚本函数func体内容
def parse_command_content(data_record_dict, manifest_file):
    if data_record_dict['command_type'] == 'bash' or data_record_dict['command_type'] == 'sh':
        func_name = data_record_dict['command_code'].split()[-1]
        # 该处做异常func 函数名判断，并对其进行二次处理
        if data_record_dict['command_code'].split('_')[0] == 'ssm':
            func_name = 'check_' + data_record_dict['command_code'].split()[-1]
        parent_path = os.path.dirname(manifest_file)
        for cli_rold in Path(parent_path).iterdir():
            if len(os.path.split(str(cli_rold))) == 2:
                if os.path.split(str(cli_rold))[1] != 'manifest.yaml':
                    command_content_old = qsli_tool.entry(cli_rold, func_name)
                    # 对func进行编码
                    data_record_dict['command_content'] = en_code(command_content_old)
    else:
        data_record_dict['command_content'] = 'None'


# 聚合封装data_record
def encapsulation_data_record_dict(scripts_path, manifest_file_list):
    data_record_dict_list = []

    for manifest_file in manifest_file_list:
        # 得到scripts目录下所有的脚本文件逐一拆解到字典列表scripts_struct_dict (可用于校验manifest.yaml内容与manifest.yaml目录结构是否对应)
        manifest_file_struct_dict = analyze_scripts_file_dir_struct(scripts_path, manifest_file)
        # print(manifest_file_struct_dict)

        with open(manifest_file, 'r', encoding='UTF-8') as f:
            # 因为 manifest.yaml文件的读取是采取 yaml.load 方式, 故manifest里面所有 #注释内容都不会写入数据库
            manifest_info = yaml.load(f, Loader=yaml.FullLoader)
            # 字段checkpoint_name：取dict的checkpoints的key作为checkpoint的value
            checkpoint_name_list = list(manifest_info['checkpoints'].keys())
            for checkpoint_name in checkpoint_name_list:
                data_record_dict = dict()
                data_record_dict['category'] = manifest_file_struct_dict['category'] # category 取值 来自于manifest script目录结构
                data_record_dict['product_name'] = manifest_info['product']   # product_name 取值
                data_record_dict['component_name']  = manifest_info['component']   # component_name 取值
                # 字段checkpoint_name：取dict的checkpoints的key作为checkpoint的value
                data_record_dict['checkpoint_name'] = checkpoint_name
                data_record_dict['status']= 'None' # status  comment '版本状态'; 初始为 None
                # 给hosttype, severity, description, tag, command_type, command_code  取值
                parse_manifest_content(data_record_dict, checkpoint_name, manifest_info)
                parse_command_content(data_record_dict, manifest_file)   # command_content comment 'func函数体' 取值

                #系统时间创建
                data_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data_record_dict['create_time'] = data_time
                data_record_dict['update_time'] = data_time
                data_record_dict_list.append(data_record_dict)
                # print(data_record)
    return  data_record_dict_list




def data_reduce_main():
    work_path = os.getcwd()
    scripts_path = os.path.join(work_path, "scripts")

    # 得到scripts目录下所有的脚本文件 (带绝对路径)
    all_file_absolute_path_list = get_all_files(scripts_path)
    # print(all_file_absolute_path_list)
    # 得到scripts目录下所有的manifest.yaml脚本文件 (带绝对路径)
    all_manifest_filelist = get_all_manifest(all_file_absolute_path_list)
    # print(all_manifest_filelist)

    #根据读取script所有manifest.yaml文件聚合封装data_record_dict
    data_record_dict_list = encapsulation_data_record_dict(scripts_path, all_manifest_filelist)

    return  data_record_dict_list

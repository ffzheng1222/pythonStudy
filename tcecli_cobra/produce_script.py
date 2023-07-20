# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : produce_script.py
# Time       ：2022/4/10 01:00
# Author     ：p_fazheng
# version    ：python 3.8
# Description：
"""

import re
import base64
import os
from pathlib import Path


MANIFEST_FILE_NAME = "manifest.yaml"


# 解码
def jm_code(command_content):
    print(command_content)
    decodestr = base64.b64decode(command_content).decode('utf-8')
    return decodestr


# 提取cli脚本内的共识函数
def func_commonbody(cli_file):
    # re.findall函数;匹配指定的字符串开头和指定的字符串结尾(前后不包含指定的字符串)
    with open(cli_file) as f :
        mark_str = re.findall('startcheck--([\s\S]*)',f.read())
        body = "".join(mark_str)
        return body

def compare_data_record(data_record_checkpoints, data_record):
    #标识记录data_record_checkpoints是否包含满足条件的data_record
    checkpoints_mark_dict = {}

    # 如果data_record_checkpoints列表为空
    if len(data_record_checkpoints) == 0:
        data_record_checkpoints.append(data_record)
    else:
        for odd_checkpoint in data_record_checkpoints:
            if (odd_checkpoint.category == data_record.category) and \
                    (odd_checkpoint.product_name == data_record.product_name) and \
                    (odd_checkpoint.component_name == data_record.component_name) and \
                    (odd_checkpoint.checkpoint_name != data_record.checkpoint_name):
                checkpoints_mark_dict[odd_checkpoint.id] = True
            else:
                checkpoints_mark_dict[odd_checkpoint.id] = False

        # 取出data_record_checkpoints所有的标识记录，如果都为True，即满足条件，追加到data_record_checkpoints列表
        if all(checkpoints_mark_dict.values()) is True:
            data_record_checkpoints.append(data_record)
        # else:
        #    print("This checkpoint data record is other component.")



# 从all_data_records列表中剔除data_record_checkpoints中的元素，并返回全新的new_data_records列表
def update_all_data_records(data_record_checkpoints, all_data_records):
    new_data_records = []
    for data_record in all_data_records:
        if data_record not in data_record_checkpoints:
            new_data_records.append(data_record)
    return  new_data_records


def write_manifest_base_context(yaml_manifest_file, path, dir_product, dir_component):
    with open('{}/{}'.format(path, yaml_manifest_file), 'w') as f:
        f.write('product: {}'.format(dir_product + "\n" +
                'component: {}'.format(dir_component) + "\n" +
                'checkpoints: ' + "\n" + "  "))
        f.close()
    return os.path.join(path, yaml_manifest_file)


def write_manifest_ckeckpoint_context(manifest_file_path, data_record_checkpoints):
    with open('{}'.format(manifest_file_path), 'a+') as f:
        for data_record in data_record_checkpoints:
            print(data_record.checkpoint_name)
            # 在解析为Unicode之后替代 \xa0 特殊空字符
            manifest_checkpoint_name = data_record.checkpoint_name.replace(u'\xa0', u' ')
            manifest_severity = data_record.severity.replace(u'\xa0', u' ')
            manifest_hosttype = data_record.hosttype.replace(u'\xa0', u' ')
            manifest_description = data_record.description.replace(u'\xa0', u' ')
            manifest_tag = data_record.tag.replace(u'\xa0', u' ')
            manifest_command_type = data_record.command_type.replace(u'\xa0', u' ')
            # manifest_command_code = data_record.command_code.replace("\'", "\"").replace(u'\xa0', u' ')
            manifest_command_code = data_record.command_code.replace(u'\xa0', u' ')
            f.write('{}: '.format(
                manifest_checkpoint_name) + "\n" + "    " +
                'severity: {}'.format(manifest_severity) + "\n" + "    " +
                'hosttype: {}'.format(manifest_hosttype) + "\n" + "    " +
                'description: {}'.format(manifest_description) + "\n" + "    " +
                'tag: {}'.format(manifest_tag) + "\n" + "    " +
                'command: ' + "\n" + "    " + "- {}".format(manifest_command_type) + "\n" + "    " + "- {}".format(manifest_command_code) + "\n" + "  ")
        f.close()


def write_cli_info(path, data_record_checkpoints):
    for data_record in data_record_checkpoints:
        cli_command_type = data_record.command_type
        cli_command_code = data_record.command_code
        # print(cli_command_type + "  ##  " + cli_command_type)
        if (cli_command_type == "bash" or cli_command_type == "sh") and len(cli_command_code.split()) > 0:
            cli_file_name = cli_command_code.split()[0]
            # print(os.path.join(path, cli_file_name))

            with open('{}/{}'.format(path, cli_file_name), 'a+') as f:
                func_name = data_record.command_code.split()[-1]
                print(data_record.command_code)
                print(func_name)
                func_content = 'function {0}()'\
                    .format(func_name) + '{' + "\n" + '{}'\
                    .format(jm_code(data_record.command_content)) + "\n" + '}' + "\n"
                print(func_content)

                f.write(func_content)
                # # 对除func之外的行进行匹配
                f.write(func_commonbody(os.path.join(path, cli_file_name)))
                f.close()

# 填写所有的script内容 (xx_cli, manifest.yaml, ...)
def write_script_info(data_record_checkpoints, mcArgus):
    dest_root_file = mcArgus['dir_tree_root_file']
    dir_category =  data_record_checkpoints[0].category
    dir_product = data_record_checkpoints[0].product_name
    dir_component = data_record_checkpoints[0].component_name

    path = Path.cwd() / dest_root_file / dir_category / dir_product / dir_component
    if os.path.exists(path) is True:
        # manifest.yaml文件创建 并 写入基础内容
        manifest_file_path = write_manifest_base_context(MANIFEST_FILE_NAME, path, dir_product, dir_component)
        # checkoutpoint内容写入manifest.yaml文件
        write_manifest_ckeckpoint_context(manifest_file_path, data_record_checkpoints)
        # cli脚本文件的创建 并 写入内容
        write_cli_info(path, data_record_checkpoints)


# 递归调用函数 作用：递归分类拆解从数据库中读取的所有data records
def classify_split_all_data_records(all_data_records, mcArgus):
    # 存放同一个 category/product/component 下不同checkpoint的数据记录
    data_record_checkpoints = []

    for data_record in all_data_records:
        # 判断data_record数据记录中的category/product/component是否与data_record_checkpoints中保持一致，其他不一致
        compare_data_record(data_record_checkpoints, data_record)

    # 开始填写script脚本文件内容信息
    if len(data_record_checkpoints) > 0:
        write_script_info(data_record_checkpoints, mcArgus)

    # print("data_record_checkpoints count:%d" %  len(data_record_checkpoints))
    # print("all_data_records count:%d" % len(all_data_records))
    all_data_records = update_all_data_records(data_record_checkpoints, all_data_records)
    if len(all_data_records) > 0:
        # print("all_data_records count:%d" % len(all_data_records))
        classify_split_all_data_records(all_data_records, mcArgus)
    else:
        print("write script finish.")
        return



def produce_script_main(all_data_records, mcArgus):
    print("...... produce_script_main ......")
    classify_split_all_data_records(all_data_records, mcArgus)

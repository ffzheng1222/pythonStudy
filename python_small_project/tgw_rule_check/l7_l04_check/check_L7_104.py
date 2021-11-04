import json
import os
import subprocess

L7_104_rule_lists = []

domain_data_file = "json_domain.txt"
rs_data_file = "json_rs.txt"





def show_match_rule(l7_domain, L7_rule):
    argv0 = l7_domain
    (status, output_sh) = subprocess.getstatusoutput('./L7_check_domain.sh ' + argv0)

    if output_sh != 'more':
        (status, output_num) = subprocess.getstatusoutput('echo ' + '"' + output_sh + '"')
        #print(output_num.split(" ")[1])
        if output_num.split(" ")[1] != '1':
            print("check_l7_104.py 传过来的domain信息：" + argv0)
            print(output_sh)
            print(L7_rule)
            print("======================================================================\n")
    else:
        (status, output_num) = subprocess.getstatusoutput('echo ' + '"' + output_sh + '"')
        print(output_num)
        # if output_num.split(" ")[1] == '1':
            # print("check_l7_104.py 传过来的domain信息：" + argv0)
            # print(output_sh)
            # print(L7_rule)
            # print("######################################################################\n")



def file_write(file, write_str=None):
    with open(file, 'a', encoding='utf-8') as fline:
        if write_str is None:
            fline.write("........\n")
        else:
            fline.write(write_str)
            fline.write("\n")
        fline.close()


def load_l7_json():
    json_file = "L7_rule_all.json"
    L7_rule_all_list = json.load(open(json_file, 'r'))

    if os.path.exists(domain_data_file):
        os.remove(domain_data_file)

    if os.path.exists(rs_data_file):
        os.remove(rs_data_file)

    for one_L7_rule in L7_rule_all_list:
        l7_vip = one_L7_rule['vip']
        if l7_vip == '172.23.36.160':
            l7_domain = one_L7_rule['domain']
            l7_rs = one_L7_rule['rs_list']
            file_write(domain_data_file, l7_domain)

            l7_rs_str = l7_domain + ' : ' + str(l7_rs)
            file_write(rs_data_file, l7_rs_str)
            # show_match_rule(l7_domain, one_L7_rule)
            # return -1


def main():
    load_l7_json()


if __name__ == "__main__":
    main()

import csv_data_ops
import os


source_data_file = "base_rules.csv"
dest_data_file = "tgw_rule.txt"
new_data_file = "cvs_domain_rs.txt"



def file_write(file, write_str=None):
    with open(file, 'a', encoding='utf-8') as fline:
        if write_str is None:
            fline.write("\n\n\n\n")
        else:
            fline.write(write_str)
            fline.write("\n")
        fline.close()


def tgw_rule_template(rule_data, rule_type):
    # 规则type & domain & appname & vip & vport & rslist
    # 规则type & appname & TCP & vip & vport & rslist
    if rule_type == "L4":
        for l4_rule_data in rule_data:
            l4_rule_str = 'add_L4&' + l4_rule_data[0] + "&" + l4_rule_data[1] + "&" + \
                       l4_rule_data[2] + "&" + str(l4_rule_data[3]) + "&" + str(l4_rule_data[4])
            file_write(new_data_file, l4_rule_str)

    elif rule_type == "L7":
        for l7_rule_data in rule_data:
            # l7_rule_str = 'add_L7&' + l7_rule_data[0] + "&" + l7_rule_data[0] + "&" + \
            #            l7_rule_data[1] + "&" + str(l7_rule_data[2]) + "&" + str(l7_rule_data[3])

            curr_rslist = '[' + l7_rule_data[3][0] + ']'
            l7_rule_str = l7_rule_data[0] + " : " + curr_rslist
            file_write(new_data_file, l7_rule_str)


def integrat_tgw_L4():
    csv_data_ops.get_tgw_l4_data()
    print(len(csv_data_ops.ok_rule_l4_data))
    # print(csv_data_ops.ok_rule_l4_data)
    tgw_rule_template(csv_data_ops.ok_rule_l4_data, "L4")


def integrat_tgw_L7():
    csv_data_ops.get_tgw_l7_data()
    print(len(csv_data_ops.ok_rule_l7_data))
    # print(csv_data_ops.ok_rule_l7_data)
    tgw_rule_template(csv_data_ops.ok_rule_l7_data, "L7")



def main():
    #integrat_tgw_L4()
    #file_write(dest_data_file)
    if os.path.exists(new_data_file):
        os.remove(new_data_file)

    print(".............L4 -- L7.................")
    integrat_tgw_L7()


#### main program ###
if __name__ == '__main__':
    main()

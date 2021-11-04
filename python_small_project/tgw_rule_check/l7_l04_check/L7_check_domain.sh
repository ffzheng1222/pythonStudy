#! /bin/bash


BASE_PATH=$(pwd)



# 原始规则文件
SRC_RULE_FILE="domain.list"



#输出带颜色字符串
function import_print(){
    local color=$2;
    #默认为红色
    local COLOR_BEGIN;
    [ "x${color}" == "x" ] && COLOR_BEGIN='\e[1;31m';
    [ "x${color}" == "xgreen" ] && COLOR_BEGIN='\e[1;32m';
    [ "x${color}" == "xred" ] && COLOR_BEGIN='\e[1;31m';
    [ "x${color}" == "xyellow" ] && COLOR_BEGIN='\e[1;33m';
    [ "x${color}" == "xblue" ] && COLOR_BEGIN='\e[0;34m';

    local COLOR_END='\e[m';

    local message=$1

    echo -e "${COLOR_BEGIN}${message}${COLOR_END}"
}



function main()
{
	import_print "check_l7_104.py 传过来的domain信息：${1}"  "yellow"
	domain_num=$(cat ${BASE_PATH}/${SRC_RULE_FILE} | grep -Hns "${1}" | wc -l)
	domain_info=$(cat ${BASE_PATH}/${SRC_RULE_FILE} | grep -Hns "${1}")
	import_print "(${domain_num}) ${domain_info}"  "red"
	echo
}



main $@
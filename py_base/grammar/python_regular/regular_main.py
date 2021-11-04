import re

def re_findall():
    s = 'rundoc 123 google 4565 \n DWADRsds 342456'
    r = re.findall('\d{3,10}?', s, re.I | re.S)


def re_finditer():
    s = 'rundoc 123 google 4565 \n DWADRsds 342456'
    r = re.finditer('\d{3,10}?', s, re.I | re.S)
    # for x in r:
    #     print(x.group(), end='\t')


def re_match():
    s = 'rundoc 123 google 4565 \n DWADRsds 342456'
    m = re.match('\w', s, re.I | re.S)
    print(m.group(), end='\t')


def re_search():
    s = 'rundoc 123 google 4565 \n DWADRsds 342456'
    s_search = re.search('\d{3,10}?', s, re.I | re.S)
    print(s_search.group(), end='\t')

def _cover(values):
    matched = values.group()
    if matched == '\n':
        matched = ''
    else:
        matched = 'python'
    return matched

def re_sub():
    s = 'rundoc 123 google 4565 \n DWADRsds 342456'
    re_s = 'python'
    # s_sub = re.sub('\d{3,10}', re_s, s, re.I | re.S)
    s_sub = re.sub('(\d{3,10})|(\n)', _cover, s, re.I | re.S)
    print(s_sub)


def re_spilt():
    s = 'rundoc 123 google 4565 \n DWADRsds 342456'
    s_split = re.split('\w+', s, re.I | re.S)
    print(s_split)


def reg_main():
    re_findall()
    re_finditer()
    re_match()
    re_search()
    re_sub()
    re_spilt()


if __name__ == '__name__':
    reg_main()

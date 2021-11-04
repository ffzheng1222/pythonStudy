from urllib import request
import re


class Spider:

    def __init__(self, url, pattern):
        self.url = url
        self.pattern = pattern

    def file_test(self, context):
        file_html = open('tony.txt', 'w')
        file_html.write(context)
        file_html.close()

    def __fetch_context(self):
        r = request.urlopen(self.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        # self.file_test(htmls)
        return htmls

    def __analysis_data(self, htmls):
        list_html = re.findall(self.pattern[0], htmls)
        # self.file_test(str(list_html))
        anchors = []
        for html in list_html:
            name = re.findall(self.pattern[1], html)
            number = re.findall(self.pattern[2], html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0][0],
            'number': anchor['number'][0]
        }
        return map(l, anchors)

    def __sort_seed(self, anchor):
        r = re.findall('\d*.\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __sort(self, anchors):
        order_anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return order_anchors

    def __show(self, order_anchors):
        for i, anchor in enumerate(order_anchors):
            print('rank %d: %s ---- %s' % (i, anchor['name'], anchor['number']))

    def go(self):
        htmls = self.__fetch_context()
        anchors = self.__analysis_data(htmls)
        anchors = self.__refine(anchors)
        order_anchors = self.__sort(anchors)
        self.__show(order_anchors)

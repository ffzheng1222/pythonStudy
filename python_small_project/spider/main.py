from Spider.spider import Spider


def main():
    # url = 'https://www.huya.com/l'
    # url = 'https://www.huya.com/g/wzry'
    # root_pattern = '<li class="game-live-item" gid="\d*" data-lp="\d*">([\s\S]*?)</li>'
    # name_pattern = '<i class="nick" title="([\s\S]*?)">([\s\S]*?)</i>'
    # number_pattern = '<i class="js-num">([\s\S]*?)</i>'

    
    url = 'https://www.binancezh.be/zh-CN/trade/BTC_USDT?layout=pro&theme=dark&type=spot'
    root_pattern = '<div class="tickerList"</div>'
    name_pattern = '<div class="tickerPriceText" title="([\s\S]*?)">([\s\S]*?)</div>'
    number_pattern = '<span style="color: rgb(248, 73, 96);">([\s\S]*?)</span>'
    

    list_pattern = [root_pattern, name_pattern, number_pattern]

    spider = Spider(url, list_pattern)
    spider.go()


#### main program ###
if __name__ == '__main__':
    main()

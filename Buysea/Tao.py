# -*- coding: utf-8 -*-
__author__ = 'fansly'

import re
import request

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"title\"\:\".*?\"', html)
        mslt = re.findall(r'\month_sales\"\:\"[\d\.]*\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            monthsales = eval(mslt[i].split(':')[1])
            ilt.append([price, title, monthsales])
        except:
            print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称", "月销量"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1], g[2]))


def main():
    goods = '礼物'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&S=' + str(48*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()

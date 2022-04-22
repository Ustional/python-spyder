import time
from time import sleep
import pandas as pd
import requests
from lxml import etree


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    html = requests.get(url, headers=headers)
    html.encoding = html.apparent_encoding
    return html.text


def parse_html(html):
    html = etree.HTML(html)
    tables = html.xpath("//div[@class='TypeList']/ul")
    # print(tables)
    for t in tables:
        imgurl = t.xpath('.//a/img/@src')
        return imgurl




for i in range(15):
    if i == 0:
        url = 'https://www.umeitu.com/bizhitupian/huyanbizhi/index.htm'
    else:
        url = 'https://www.umeitu.com/bizhitupian/huyanbizhi/index_{}.htm'.format(i)
    # print(url)
    # print('https://www.umeitu.com/bizhitupian/huyanbizhi/index_{}.htm'.format(i))
    sleep(1)
    html = get_html(url)
    print(parse_html(html))

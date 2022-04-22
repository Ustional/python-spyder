# 1. 导入库包
import requests
from lxml import etree
from time import sleep
import os
import pandas as pd
import re

BOOKS = []
IMGURLS = []


# 2. 获取网页源代码
def get_html(url):
    global html
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    # 异常处理
    try:
        html = requests.get(url, headers=headers)
        # 声明编码方式
        html.encoding = html.apparent_encoding
        # 判断
        if html.status_code == 200:
            print('成功获取源代码')
            # print(电影.html.text)
    except Exception as e:
        print('获取源代码失败：%s' % e)
    # 返回html
    return html.text


# 3. 解析网页源代码
def parse_html(html):
    html = etree.HTML(html)
    # 每个图书信息分别保存在 class="indent" 的div下的 table标签内
    tables = html.xpath("//div[@class='indent']//table")
    # print(len(tables))  # 打印之后如果是25的话就是对的
    books = []
    imgUrls = []

    # 遍历通过xpath得到的li标签列表
    # 因为要获取标题文本，所以xpath表达式要追加 /text(), t.xpath返回的是一个列表，且列表中只有一个元素所以追加一个[0]
    for t in tables:
        # title = t.xpath(".//div[@class='p12']/a/@title")  # 匹配得到的是空的
        # 书名
        title = t.xpath(".//td[@valign='top']//a/@title")[0]
        # 链接
        link = t.xpath(".//td[@valign='top']//a/@href")[0]

        # 获取pl标签的字符串
        pl = t.xpath(".//td[@valign='top']//p[1]/text()")[0]

        # 截取国家
        if '[' in pl:
            country = pl.split('[')[1].split(']')[0]
        else:
            country = '中'  # 没有国家的默认为“中国”

        # 截取作者
        if '[' in pl:
            author = pl.split(']')[1].split('/')[0].replace(" ", "")
        elif len(pl.split('/')) == 3:
            author = '无'
        elif '[' not in pl:
            author = pl.split('/')[-4].replace(" ", "")
        else:
            author = '无'

        # 截取翻译者
        if '[' in pl:
            translator = pl.split('/')[-4].replace(" ", "")
        elif len(pl.split('/')) == 3:
            translator = ' '
        else:
            translator = ' '

        # 截取出版社
        publisher = pl.split('/')[-3]
        # 截取出版时间
        time = pl.split('/')[-2]

        # 截取单价
        if '元' in pl:
            price = pl.split('/')[-1].split('元')[0]
        else:
            price = pl.split('/')[-1]

        # 获取星级数
        str1 = t.xpath(".//td[@valign='top']//div[@class='star clearfix']/span[1]/@class")[0].replace("allstar", "")
        # 此时获取到的数字其实是字符串类型，不能直接%10，需要把str转化为int
        num = int(str1)
        star = num / 10
        # 获取评分
        score = t.xpath(".//td[@valign='top']//div[@class='star clearfix']/span[2]/text()")[0]
        # 获取评价人数
        pnum = t.xpath(".//td[@valign='top']//div[@class='star clearfix']/span[3]/text()")[0]
        people = re.sub("\D", "", pnum)

        # 获取简介
        comments = t.xpath(".//p[@class='quote']/span/text()")
        comment = comments[0] if len(comments) != 0 else "无"

        book = {
            '书名': title,
            '链接': link,
            '国家': country,
            '作者': author,
            '翻译者': translator,
            '出版社': publisher,
            '出版时间': time,
            '价格': price,
            '星级': star,
            '评分': score,
            '评价人数': people,
            '简介': comment
        }

        # 图片
        imgUrl = t.xpath(".//a/img/@src")[0]
        # print(imgUrl)

        books.append(book)
        imgUrls.append(imgUrl)

    return books, imgUrls


# 4. 下载图片保存文件
def downloadimg(url, book):
    # 判断文件夹是否在指定路径下面,建立文件夹并把指定路径移到文件夹下面
    if 'bookposter' in os.listdir(r'C:\Users\liangsui\PycharmProjects\pythonProject\DoubanMovies'):
        pass
    else:
        os.mkdir(r'C:\Users\liangsui\PycharmProjects\pythonProject\DoubanMovies\bookposter')
    os.chdir(r'C:\Users\liangsui\PycharmProjects\pythonProject\DoubanMovies\bookposter')
    # 返回img的二进制流
    img = requests.request('GET', url).content

    with open(book['书名'] + '.jpg', 'wb') as f:
        # print('正在下载: %s' % url)
        f.write(img)


# 5. 数据预处理
# def processData():

if __name__ == '__main__':
    # url = 'https://book.douban.com/top250?start=0'
    # 10页循环遍历
    for i in range(10):
        # 2. 定义url并获取网页源代码
        url = 'https://book.douban.com/top250?start={}'.format(i * 25)
        # print(url)
        html = get_html(url)
        # 3. 解析网页源代码
        sleep(1)
        books = parse_html(html)[0]
        imgUrls = parse_html(html)[1]

        BOOKS.extend(books)
        IMGURLS.extend(imgUrls)

    # 4. 下载图片保存文件
    for i in range(250):
        # sleep(1)
        downloadimg(IMGURLS[i], BOOKS[i])

    os.chdir(r'C:\Users\liangsui\PycharmProjects\pythonProject\DoubanMovies')

    # 以csv格式写入本地
    bookdata = pd.DataFrame(BOOKS)
    bookdata.to_csv('book.csv', index=False)
    print("图书信息写入本地成功")

    # 以txt格式写入本地错误
    # 得到的是字典格式，要想写成txt格式需要先转化成字符串格式
    # for i in range(25):
    #     with open('book.txt', 'a') as f:
    #         f.write(books[i] + '\n')

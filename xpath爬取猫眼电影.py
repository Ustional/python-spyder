import requests
from lxml import etree

with open('电影.html', 'r', encoding='utf-8') as f:
    html = f.read()


# print(html) def get_html(url): headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36' } html = requests.get(url,
# headers=headers) html.encoding = html.apparent_encoding return html.text


def parse_html(html):
    html = etree.HTML(html)
    print(html)
    tables = html.xpath('//dl[@class="movie-list"]/dd')
    # print(tables)
    for t in tables:
        imgsrc = t.xpath('.//div[@class="movie-item film-channel"]/a/div/img[2]/@src')
        title = t.xpath('.//div[@class="channel-detail movie-item-title"]/@title')
        titles = "".join(title).strip()
        # print("".join(title).strip())
        # print(imgsrc)
        kind = t.xpath('.//div[@class="movie-hover-info"]/div[2]/text()')
        kinds = "".join(kind).strip()
        # print("".join(kind).strip())
        protagonis = t.xpath('.//div[@class="movie-hover-info"]/div[3]/text()')
        protagoni = "".join(protagonis).strip()
        # print("".join(protagonis).strip())
        time = t.xpath('.//div[@class="movie-hover-info"]/div[4]/text()')
        times = "".join(time).strip()
        # print("".join(time).strip())
        score = t.xpath('.//div[@class="channel-detail channel-detail-orange"]/i[1]/text()')
        score1 = t.xpath('.//div[@class="channel-detail channel-detail-orange"]/i[2]/text()')
        scores = "".join(score) + ",".join(score1)
        print('电影名称：', titles, '类型：', kinds, '主演：', protagoni, '上映时间：', times, '评分：', scores)
        print('***********************************')


# html = get_html('https://www.maoyan.com/films?showType=3')
parse_html(html)

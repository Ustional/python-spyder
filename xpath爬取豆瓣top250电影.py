from time import sleep
import pandas as pd
import requests
from lxml import etree



MOVIES = []

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    html = requests.get(url, headers=headers)
    html.encoding = html.apparent_encoding
    return html.text


def parse_html(html):
    html = etree.HTML(html)
    # print(html)
    tables = html.xpath("//ol[@class='grid_view']//li")
    # print(len(tables))
    movies = []
    for t in tables:
        title = t.xpath(".//div[@class='info']//span[1]/text()")[0]
        # print(title)
        director = t.xpath(".//div[@class='bd']/p/text()")[0]
        # print(director)
        score = t.xpath(".//div[@class='star']/span[2]/text()")[0]
        # print(score)
        movie = {
            '电影': title,
            '导演': director,
            '评分': score
        }
        movies.append(movie)
    return movies

# 电影.html = get_html('https://movie.douban.com/top250')
# parse_html(电影.html)


# if __name__ == '__main__':
#     for i in range(10):
#         url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
#         # print(url)
#         html = get_html(url)
#         sleep(1)
#         movies = parse_html(html)
#         # print(movies)
#         MOVIES.extend(movies)
#     # print(MOVIES)
#
#     moviedata = pd.DataFrame(MOVIES)
#     moviedata.to_csv('movies.csv')
#     print("图书信息写入本地成功")


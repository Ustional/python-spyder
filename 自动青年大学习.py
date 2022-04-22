import requests
from lxml import etree

#  获取青年大学习网页的响应
response = requests.get('https://news.cyol.com/gb/channels/vrGlAKDl/index.html')
#  与网页编码一致
response.encoding = response.apparent_encoding
html = response.text
#  用xpath分析网页
html = etree.HTML(html)
href = html.xpath('//ul[@class="movie-list"]/li[1]/h3/a/@href')[0].split('/')[0:-1]
link = '/'.join(href) + '/images/end.jpg'
img = requests.get(link)
# 将图片保存在文件夹里面
with open('./青年大学习/' + '最新青年大学习' + '.jpg', 'wb') as fp:
    fp.write(img.content)
    print('最新青年大学习下载成功')
# table = html.xpath('//ul[@class="movie-list"]/li')
# count = 0
# for t in table:
#     count += 1
#     href1 = t.xpath('./h3/a/@href')[0]
#     # print(href1)
#     href = t.xpath('./h3/a/@href')[0].split('/')[0:-1]
#     link = '/'.join(href) + '/images/end.jpg'
#     # print(link)
#     title = t.xpath('./h3/a/text()')[0]
#     # print(title)
#     img = requests.get(link)
#     with open('./青年大学习/' + str(count) + '.jpg', 'wb') as fp:
#         fp.write(img.content)
#         print('正在下载第%d张图片' % count)

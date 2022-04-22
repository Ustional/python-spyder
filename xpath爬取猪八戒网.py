import requests
from lxml import etree


url = 'https://hengyang.zbj.com/wzkf/f.html?fr=zbj.sy.zylm'
response = requests.get(url)
html = response.text
# print(html)
htmls = etree.HTML(html)
# print(htmls)
table = htmls.xpath('//div[@class="new-service-wrap"]/div')
for t in table:
    company = t.xpath('.//p[@class="text-overflow"]/a/text()')[0]
    # print(company)
    title = t.xpath('.//p[@class="title"]/a/text()')
    title = "".join(title)
    # print(title)
    price = t.xpath('.//div[@class="service-price clearfix"]/span[1]/text()')[0].replace('¥','')
    # print(price)
    print('公司：', company, '\n项目：', title, '\n价格：', price)
    print('**************************************************')
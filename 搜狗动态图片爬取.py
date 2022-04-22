import requests
import json
import os
url = 'https://pic.sogou.com/napi/pc/searchList?mode=13&dm=4&cwidth=1920&cheight=1080&start=0&xml_len=192&query=%E5%A3%81%E7%BA%B8'
# print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
html = requests.get(url,headers=headers)
# print(html)
html = json.loads(html.text)
# print(html)
img_urls = []
jd = html['data']['items']
# print(jd)
for i in jd:
    imgurl = i['oriPicUrl']
    # print(imgurl)
    img_urls.append(imgurl)


count = 0
for t in img_urls:
    count += 1
    # print('.'+t[-3::])
    try:
        img = requests.get(t,headers=headers)
        print('正在下载：', t)
    except:
        print('下载不了',t)
        continue
    with open('img/'+str(count)+'.jpg','wb')as f:
            f.write(img.content)
print('下载好了')


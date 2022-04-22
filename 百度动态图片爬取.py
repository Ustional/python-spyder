import requests
import json

url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7691498335796988978&ipn=rj&ct=201326592&is=&fp' \
      '=result&fr=&word=%E5%A3%81%E7%BA%B8&cg=wallpaper&queryWord=%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8' \
      '&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode' \
      '=&nojc=&isAsync=&pn=90&rn=30&gsm=5a&1648522748575= '
print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.51 Safari/537.36 '
}
html = requests.get(url, headers=headers)
# print(html)
html = json.loads(html.text)
# print(html)
img_urls = []
jd = html['data']
# print(len(jd))
for i in jd[0:30]:
    imgurl = i['thumbURL']
    # print(imgurl)
    img_urls.append(imgurl)
    # print(img_urls)

count = 0
for t in img_urls:
    count += 1
    # print('.'+t[-3::])
    try:
        img = requests.get(t, headers=headers)
        print('正在下载：', t)
    except:
        print('下载失败：', t)
        continue
    with open('img1/' + str(count) + '.jpg', 'wb') as f:
        f.write(img.content)
print('下载好了')

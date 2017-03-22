﻿import requests
import json
import urllib

def getSogouImag(category,length,path):
    n = length
    cate = category
    imgs = requests.get('http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n))
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        imgs_url.append(j['bthumbUrl'])
    m = 0
    for img_url in imgs_url:
            print('***** '+str(m)+'.jpg *****'+'   Downloading...')
            urllib.request.urlretrieve(img_url,path+str(m)+'.jpg')
            m = m + 1
    print('Download complete!')
getSogouImag('壁纸',20,'d:/download/')


'''
***** 0.jpg *****   Downloading...
***** 1.jpg *****   Downloading...
***** 2.jpg *****   Downloading...
***** 3.jpg *****   Downloading...
***** 4.jpg *****   Downloading...
***** 5.jpg *****   Downloading...
***** 6.jpg *****   Downloading...
***** 7.jpg *****   Downloading...
***** 8.jpg *****   Downloading...
***** 9.jpg *****   Downloading...
***** 10.jpg *****   Downloading...
***** 11.jpg *****   Downloading...
***** 12.jpg *****   Downloading...
***** 13.jpg *****   Downloading...
***** 14.jpg *****   Downloading...
***** 15.jpg *****   Downloading...
***** 16.jpg *****   Downloading...
***** 17.jpg *****   Downloading...
***** 18.jpg *****   Downloading...
***** 19.jpg *****   Downloading...
Download complete!
'''
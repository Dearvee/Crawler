import requests
from bs4 import BeautifulSoup
url = 'https://git.ahstu.cc/explore/users?page='
n = 9
user_count=0
for x in range(1,n):
    res = requests.get(url+str(x))
    soup = BeautifulSoup(res.text,'html.parser')
    for i in soup.select('.item'):
        if len(i.select('.header a')) > 0:
            user_name = i.select('.header a')[0].text
            user_count=user_count+1
            print(user_name)
print(user_count)
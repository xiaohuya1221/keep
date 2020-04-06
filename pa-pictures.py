import requests
import urllib.request
from bs4 import BeautifulSoup
import threading

def down_pics(link):
    print(link,'--------linking\n')
    filename = link.split('/')[-1]
    retries = 0
    while retries < 3:
        try:
            # urllib.request.urlretrieve(link,'pics/'+filename)
            pics = requests.get(link, timeout=30)
            with open('pics/' + filename, 'wb') as f:
                f.write(pics.content)  # 用content，不用text！！！
        except requests.exceptions.RequestException as e:
            print(e)
            print(link, 'fail')
            retries += 1
        else:
            print(link, 'succeed')
            break

url = 'https://www.qiushibaike.com/imgrank/page/7'
for i in range(3):
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html,'lxml')
    result = soup.find_all('div',class_="thumb")

    current_page = soup.find_all('span',class_="current")
    cur_page = int(current_page[0].text)
    next_page = cur_page - 1
    print('========this in the page %d========'%cur_page)

    for j in result:
        link = j.img['src']
        link = 'https:' + link
        k = threading.Thread(target=down_pics,args=(link,))  # link后面要加逗号
        k.start()

    url = 'https://www.qiushibaike.com/imgrank/page/%d'%next_page
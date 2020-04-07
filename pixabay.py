import requests
from bs4 import BeautifulSoup
import threading

def pic_down(link):
    retries = 0
    while retries < 3:
        retries += 1
        print(link,'downing---')
        try:
            req = requests.get(link,timeout=30)
            pic = req.content
            list_name = link.split('/')[-3:]
            pic_name = '.'.join(list_name)
            with open('pics/'+pic_name,'wb') as f:
                f.write(pic)
        except requests.exceptions.RequestException as e:
            print(e)
            print(pic_name,'failed')
        else:
            print(pic_name,'succeed')
            break

url = 'https://www.lifeofpix.com/page/20/?display=small&content=all'
for i in range(3):
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html,'lxml')
    result = soup.find_all('a',class_="download")

    for link in result:
        link = link.get('download')
        t = threading.Thread(target=pic_down,args=(link,))
        t.start()

    current = soup.find('div',class_="numbers")
    next = current.find('a')
    url = next.get('href')









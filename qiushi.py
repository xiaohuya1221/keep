import requests
from lxml import etree

url = 'https://www.qiushibaike.com/text/page/10/'
data_all = ''
for a in range(3):
    content = requests.get(url)
    conts = content.text

    tree = etree.HTML(conts)
    result = tree.xpath('//div[@class="content"]')
    current_page = tree.xpath('//li/span[@class="current"]/text()')

    cur_page = int(current_page[0].strip())
    next_page = cur_page-1
    url = 'https://www.qiushibaike.com/text/page/%d/'%next_page

    data = '======contents in the page %d====== \n\n'%cur_page

    for div in result:
        # author
        author = div.xpath('../../div[@class="author clearfix"]/a/h2/text()')
        aut = author[0].strip()
        data += (aut+' ---')
        # sex
        sex = div.xpath('../../div[@class="author clearfix"]/div/@class')
        if sex[0] == 'articleGender womenIcon':
            data += 'women ---'
        else:
            data += 'man ---'
        # grade
        grade = div.xpath('../../div[@class="author clearfix"]/div/text()')
        data += '等级（'+grade[0]+'）---'
        # ‘好笑’number
        haoxiao = div.xpath('../../div[@class="stats"]/span[@class="stats-vote"]/i[@class="number"]/text()')
        data += '好笑数（'+haoxiao[0]+'）---'
        # '评论’number
        comments = div.xpath('../../div[@class="stats"]/span[@class="stats-comments"]/a/i/text()')
        data += '评论数（'+comments[0]+'）---\n'
        # contents
        contents = div.xpath('span/text()')
        for i in contents:
            j = i.strip()
            data += (j+'\n\n')
    data += '\n\n'
    data_all += data
# 写入
with open('data.txt','w',encoding='utf-8') as f:
    f.write(data_all)


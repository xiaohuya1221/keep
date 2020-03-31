import requests
import re
import time

# 读取已有用户信息放到dic中备用
with open('users_data.txt',encoding='utf-8') as f:
    list_lines = f.readlines()
    dic = {}
    for i in list_lines:
        if i:
            list_line = i.split()
            dic[list_line[0]] = list_line[1:]

#收集用户名
name = input('请输入用户名（新用户输入用户名默认创建用户信息）：\n')
while True:
    name_rule = re.compile(r'\S{2,20}')
    mat = name_rule.match(name)
    if mat:
        break
    else:
        print('用户名无效（有效用户名为2-20个非空格字符）')
        name = input('请重新输入：')

#通过用户名在dic中获取或添加用户数据
try:
    if dic[name]:
        list_data = dic[name]
except:
    list_data = ['0','0','0']
print('亲爱的%s,您已经玩了%s次，最少%s轮猜出答案，平均%s轮猜出答案。\
游戏即将开始，祝您游戏愉快！'%(name,list_data[0],list_data[1],list_data[2]))
print()
time.sleep(1)

#终于开始猜了
t = 0
while True:
    t += 1
    num = requests.get('https://python666.cn/cls/number/guess/')
    number = int(num.text)
    r = 0
    while True:
        r += 1
        try:
            answer = int(input('请输入您的答案(1-100的整数）：'))
            if answer < number:
                print('猜小了，再猜猜看')
            elif answer > number:
                print('猜大了，再猜猜看')
            elif answer == number:
                print('猜对了，您一共猜了%d轮' % r)
                break
        except:
            print('无效答案')
    con = input('是否继续游戏（y继续，其他结束)')
    print()
    if con != 'y':
        print('游戏结束，欢迎再来！')
        break

#猜完了，开始更新文档中的数据
list_data[1] = str(r+int(list_data[1]))
list_data[0] = str(t+int(list_data[0]))
list_data[2] = '%.2f'%(int(list_data[1])/int(list_data[0]))
dic[name] = list_data
with open('users_data.txt','w',encoding='utf-8') as file:
    for n in dic:
        user_data = dic[n]
        user_data.insert(0,n)
        str_user = ' '.join(user_data)
        file.write(str_user+'\n')

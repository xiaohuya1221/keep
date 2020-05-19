import requests

def guess_one_time():
    num = int(requests.get('https://python666.cn/cls/number/guess/').text)
    round = 0  # 记录猜中一次的轮数
    while True:
        guess = int(input('please guess a number from 1 to 100:'))
        round += 1
        if guess > num:
            print('too big,guess again')
        elif guess < num:
            print('too small,guess again')
        else:
            print('bingo,you have guessed %d times' % round)
            break
    return round

def guess_times(times=0,count=0,min_round=0):
    whether = 'y'
    while whether == 'y':
        times += 1
        round = guess_one_time()
        count += round
        if min_round == 0 or min_round > round:
            min_round = round
        else:
            pass
        print(user_name + ',you have played %d times,%d rounds is the fastest,%.2f rounds is in average.' % (times, min_round, count / times))
        whether = input('"y" is continue and others are not:')
    print('game is over,welcome again')
    return times,count,min_round


# 读数据并改成字典形式
dic = {}
with open('game_one_user.txt','r') as file:
    data = file.readlines()
    for i in data:
        if i :     # 清除空行
            one_list = i.split()
            one_list = [j for j in one_list if j]    # 清除空格
            dic[one_list[0]] = one_list[1:]

# 查看是新用户还是老用户,并输出历史数据,加猜的函数
user_name = input('what is your name:')
if dic.get(user_name):
    count = int(dic[user_name][2])  # 总轮数
    times = int(dic[user_name][0])  # 记录次数
    min_round = int(dic[user_name][1])
    print(user_name + ',you have played %d times,%d rounds is the fastest,%.2f rounds is in average.Start!' % (times, min_round, count/times))
    times,count,min_round = guess_times(times,count,min_round)
else:
    dic[user_name] = ['0','0','0']
    print(user_name + ',you have played 0 time,0 round is the fastest,0 round is in average.Start!')
    times,count,min_round = guess_times()

# 写入数据
dic[user_name] = [str(times),str(min_round),str(count)]
user_list = []
for k in dic:
    user_data = '%s  %s  %s  %s\n' %(k,dic[k][0],dic[k][1],dic[k][2])
    user_list.append(user_data)
with open('game_one_user.txt','w') as f:
    f.writelines(user_list)

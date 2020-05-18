from random import randint

# 读数据并改成字典形式
dic = {}
with open('game_one_user.txt','r') as file:
    data = file.readlines()
    for i in data:
        if i :     # 清除空行
            one_list = i.split()
            one_list = [j for j in one_list if j]    # 清除空格
            dic[one_list[0]] = one_list[1:]

# 查看是新用户还是老用户,并输出历史数据
user_name = input('what is your name:')
try:
    dic[user_name]
    print(user_name + ',you have played %s times,%s rounds is the fastest,\
%.2f rounds is in average.Start!' % (dic[user_name][0], dic[user_name][1], int(dic[user_name][2]) / int(dic[user_name][0])))
except KeyError:
    dic[user_name] = ['0','0','0']
    print(user_name + ',you have played 0 time,0 round is the fastest,0 round is in average.Start!')

# 开始猜
count = int(dic[user_name][2])   # 总轮数
times = int(dic[user_name][0])   # 记录次数
min_round = int(dic[user_name][1])
whether = 'y'
while whether == 'y':
    num = randint(1, 100)
    times += 1
    round = 0    # 记录猜中一次的轮数
    while True:
        guess = int(input('please guess a number from 1 to 100:'))
        round += 1
        count += 1
        if guess > num:
            print('too big,guess again')
        elif guess < num:
            print('too small,guess again')
        else:
            print('bingo,you have guessed %d times' % round)
            if min_round == 0 or min_round > round:
                min_round = round
            else:
                pass
            print(user_name+',you have played %d times,%d rounds is the fastest,%.2f rounds is in average.' %(times,min_round,count/times))
            whether = input('"y" is continue and others are not:')
            break
print('game is over,welcome again')


dic[user_name] = [str(times),str(min_round),str(count)]
user_list = []
for k in dic:
    user_data = '%s  %s  %s  %s\n' %(k,dic[k][0],dic[k][1],dic[k][2])
    user_list.append(user_data)
with open('game_one_user.txt','w') as f:
    f.writelines(user_list)

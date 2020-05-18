from random import randint

name = input('what is your name:')
count = 0   # 总轮数
times = 0   # 记录次数
min_round = 0
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
            if min_round ==0 or min_round > round:
                min_round = round
            else:
                pass
            print(name+',you have played %d times,%d rounds is the fastest,%.2f rounds is in average.'%(times,min_round,count/times))
            whether = input('"y" is continue and others are not:')
            break
print('game is over,welcome again')

data = '%s  %d  %d  %d \n'%(name,times,min_round,count)
with open('game_one_user.txt','a') as f:
    f.write(data)

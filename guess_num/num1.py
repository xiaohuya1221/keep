
from random import randint

num = randint(1,100)
c = 0
while True:
    guess = int(input('please guess a number from 1 to 100:'))
    c += 1
    if guess > num:
        print('too big,guess again')
    elif guess < num:
        print('too small,guess again')
    else:
        print('bingo,you have guessed %d times' %c)
        break
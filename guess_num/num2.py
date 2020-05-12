
from random import randint

# while True:
#     num = randint(1, 100)
#     c = 0
#     while True:
#         guess = int(input('please guess a number from 1 to 100:'))
#         c += 1
#         if guess > num:
#             print('too big,guess again')
#         elif guess < num:
#             print('too small,guess again')
#         else:
#             print('bingo,you have guessed %d times' %c)
#             whether = input('"y" is continue and others are not:')
#             break
#     if whether == 'y':
#         continue
#     else:
#         break
# print('game is over,welcome again')

whether = 'y'
while whether == 'y':
    num = randint(1, 100)
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
            whether = input('"y" is continue and others are not:')
            break
print('game is over,welcome again')
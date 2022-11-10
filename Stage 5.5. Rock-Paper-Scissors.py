import random


def get_type_game():
    user_opt = input()
    if user_opt:
        return user_opt.split(',')
    else:
        return ['rock', 'paper', 'scissors']


def get_rating():
    file = open('rating.txt', 'r')
    a = 0
    for line in file:
        name_user, score_user = line.split()
        if name_user == name:
            a = int(score_user)
    return a


def who_win():
    wins_user = []
    for n in range(1, len(options) // 2 + 1):
        wins_user.append(options[options.index(user)-n])

    if user == comp:
        winner = 'draw'
        print('There is a draw', comp)
        return 50
    elif comp in wins_user:
        winner = 'user'
        print('Well done. The computer chose', comp, 'failed')
        return 100
    else:
        winner = 'comp'
        print('Sorry, but the computer chose', comp)
        return 0


name = input('Enter your name: ')
print('Hello, ' + name)
rating = get_rating()
options = get_type_game()
print("Okay, let's start")

while True:
    user = input()
    comp = options[random.randint(0, len(options)-1)]
    if user in options:
        rating += who_win()
    else:
        if user == '!rating':
            print('Your rating:', rating)
        elif user == '!exit':
            break
        else:
            print('Invalid input')
            continue

print('Bye!')

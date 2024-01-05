import random


def gen():
    return random.randint(1, 10)


def check(user_guess, correct_number):
    if user_guess < correct_number:
        print('low')
    elif user_guess > correct_number:
        print('high')
    else:
        print('correct')


correct_number = gen()
user_guess = int(input())

while user_guess != correct_number:
    user_guess = int(input())
    check(user_guess, correct_number)

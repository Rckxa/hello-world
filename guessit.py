import random


def gen():
    return random.randint(1, 10)


def check(guess, correct):
    if guess < correct:
        print('low')
    elif guess > correct:
        print('high')
    else:
        print('correct')


correct_number = gen()
print("Am thinking of a number from 1-10,guess the correct number")
user_guess = int(input())

while user_guess != correct_number:
    user_guess = int(input())
    check(user_guess, correct_number)



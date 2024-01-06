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
user_guess = int(input())

while user_guess != correct_number:
    user_guess = int(input())
    check(user_guess, correct_number)

#added a new function
def do_nothing():
    return 0

def second_function():
    return 0 #this function also does nothing but will be merged
            # to master because what the hell

#new line 1 by his branch
# comment added by hers branch
# ok last one

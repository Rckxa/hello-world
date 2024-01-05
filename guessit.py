import random

def check(user_guess, correct_number):
    user_guess = int(input())
    if(user_guess < correct_number):
        print('low')
    elif(user_guess > correct_number):
        print('high')
    else:
        print('correct')
def gen():
    return random.randint(1, 10)

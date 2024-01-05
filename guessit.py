def gen():
    #generate a random number
    return random.randint(1, 10)

# our variables
correct_number = gen();
user_guess = int(input("Enter a number \n"))

import random
number = random.randint(1, 100)
guess_count = 0

while True:
    guess = int(input ("Guess a number: "))
    guess_count += 1
    if guess > 100 or number < 1:
        print ("Not a valid input")
    else: 
        if number == guess:
            print ("You guessed it!!")
            print ("It took you", guess_count,"guesses.")
            break
        elif number > guess:
            print ("The numbers bigger than that\n")
        elif number < guess:
            print ("The numbers less than that\n")
    


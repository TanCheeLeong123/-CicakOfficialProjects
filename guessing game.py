import random
myname = input("What's your name? ")
print("Hi, " + myname + ", I am thinking of a number between 100 to 999.")

a = random.randint(100, 999)
attempts = 0

while attempts < 10:
    try:
        guess = int(input("Guess your number from 100 to 999. "))
        attempts += 1

        if guess < 100 or guess > 999:
            print("Please enter the number from 100 to 999.")
        elif guess < a:
            print("Too low! Try again.")
        elif guess > a:
            print("Too high! Try again.")
        else:
            print("You guessed the number " + str(a) + " in " + str(attempts) + " attempts.")
            break
        if attempts == 10:
            print('Nope. The number I was thinking of was ' + str(a) + '.')
            break
    except ValueError:
        print("Please enter a valid integer.")
    

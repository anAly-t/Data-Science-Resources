# Practice Exercise 3: Guess the Number

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 10
    
    print("Welcome to Guess the Number game!")
    print("I have selected a number between 1 and 100. You have 10 attempts to guess it.")
    
    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly.")
            return
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
        
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    
    print(f"Sorry, you've used all your attempts. The correct number was {secret_number}.")

# Call the function to play the game
guess_the_number()

import random

def guess(num_guesses, random_number):
    
    num_guesses = num_guesses
    random_number = random_number
    user_guess = input("Please enter a guess: ")

    try:
        converted_guess = int(user_guess)
    except ValueError:
        print("This is a non-number value, please try again")
        guess(num_guesses, random_number)
       


    if converted_guess == random_number:
        num_guesses += 1
        print("Congrats You WIN!!! You had ", num_guesses, "guesses")
    else:
        num_guesses += 1
        if converted_guess > random_number:
            print("Wrong. The number is lower...")
        if converted_guess < random_number:
            print("Wrong. The number is higher...")
        guess(num_guesses, random_number)

    
def main():

    random_number = random.randint(0, 100)
    num_guesses = 0
    guess(num_guesses, random_number)




if __name__ == "__main__":
    main()

import random

correct_number = random.randint(1, 10)

print("Welcome to the guessing game!")

def my_guessing_game():
    trials = 5
    print("All you have to do is guess correctly the number that I picked between 1 and 100 but you only have 5 tries...BEGIN")
    while trials > 0:        
        attempt = int(input("Enter your best guess: "))
        if attempt == correct_number:
            print("We have our winner!!!!!.")
            break
        else:
            print("Sorry,try again.")
            trials -= 1
            if trials > 0:
                print(f"You have {trials} {'trials' if trials > 1 else 'try'} remaining.")
    if trials == 0:
        print(f"Sadly, you run out of trials.The correct number was {correct_number}.")


my_guessing_game()




import random

correct_number = random.randint(1, 100)

print("Welcome to the guessing game!")

def my_guessing_game():

    trials = 5

    game_running = True
  
    player_info = {'name': '', 'trials': 0, 'correct_number': False}
  
    player_info['name'] = input("Enter your name: ")
  
    print(f"Hi, {player_info['name']}! I have selected a number between 1 and 100. Can you guess it?")

    while game_running:
        trial = int(input("Enter your attempt: "))
        if trial == correct_number:
            print(f"Congratulations, {player_info['name']}! You guessed the correct number.")
            player_info['correct_number'] = True
            break
        else:
            print("Incorrect guess. Try again.")
            trials -= 1
            player_info['trials'] += 1
            if trials > 0:
                print(f"You have {trials} {'attempts' if trials > 1 else 'trials'} remaining.")
            else:
                print(f"Sorry, {player_info['name']}, you've run out of trials. The correct number was {correct_number}.")
                break

    
    print("\nPlayer Information:")
    print(f"Name: {player_info['name']}")
    print(f"Attempts: {player_info['trials']}")
    print("Game Status: " + ("Win" if player_info['correct_number'] else "Loss"))

my_guessing_game()

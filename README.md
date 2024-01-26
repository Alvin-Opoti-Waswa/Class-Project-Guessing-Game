# THE GUESSING GAME

## HOW IT WORKS:
This is a guessing game.It uses modules to generate a random number between 1 and 100 represented as correct_number.
The function gives the player 5 trials and informs him to find the correct answer before the trials end.
The user then enters his?her guesses, and the program checks if it is correct. If the guess is correct, the program prints a winning message.
Otherwise, it informs the user to try again. If the user runs out of trials, the code prints the correct number.

## HOW TO USE IT:
Attempt the correct answer.

## WHAT'S NEW WITH THE UPDATE 2.0
The update starts by importing the "random" module to generate a random number. Then, the program selects a random number between 1 and 100. The user is asked to input their name. After this, the game begins, and the user is prompted to guess the correct number. The user has 5 attempts to guess the correct number. After each attempt, the program informs the user whether their guess was correct or not. Once the user has used all of their attempts, the game ends, and the outcome is displayed, indicating whether the player won or lost.

## WHAT'S NEW WITH THE UPDATE 3.0
The code now defines a class called GuessingGame to create a simple number guessing game. When an instance of GuessingGame is created, it takes the player's name and an optional maximum number of attempts as parameters. Inside the class, a random number between 1 and 10 is generated and stored as the secret number. The class contains a method called play_game, which allows the player to input their guesses. The game provides feedback on whether the guess is correct or not, and allows a limited number of attempts before revealing the correct number and ending the game. After playing the game, the player's information and game status (win or loss) are displayed.

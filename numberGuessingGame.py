import random

# holds a print statement to print the title at the start of the game
def display_title():
    print("\nThis is a guessing game. It will randomly select a number between 1 and 10. It will then\n"
          "promt the user for input to try and guess what that number is. After each guess the user will \n"
          "receive as prompt telling them if they were \"too high\" or \"too low\". When the user guesses\n"
          "the right number they will be informed and asked if they would like to play again. The game will\n"
          "continue until the user decides to quit\n")

def play_game(targetNumber, counter):
    # plays the game

    while True:
        # check for invalid input
        try:
            if counter == 1:
                # take user input and convert to an int
                playerGuess = int(input("\nOk! Lets give it a go. Please choose a number between 1 and 10: "))
                counter += 1
            elif counter >= 2:
                # change input prompt when counter is at or above 2
                playerGuess = int(input("\nLets try again. Please choose a number between 1 and 10: "))
        except ValueError:
            print("Please enter a valid response.")
        else:
            # check to make sure input is between 1 and 10
            if 1 > playerGuess > 10:
                print("Please pick a number between 1 and 10.")

            elif 1 <= playerGuess <= 10:
                # check to see if guess is between 1 and 10 and if its high or low compared to the answer and
                # respond accordingly

                if playerGuess > targetNumber:
                    # user guessed too high
                    print("Sorry that is too high!")

                elif playerGuess < targetNumber:
                    # user guessed too low
                    print("Sorry that is too low!")

                elif playerGuess == targetNumber:
                    # user guessed correctly
                    print("Good job %i was the right number!" % targetNumber)
                    return

                else:
                    # checking for unexpected input
                    print("Invalid input. Please try again")

            else:
                # error catching in case something weird happens
                print("Invalid input. Please try again.")

def main():
    # runs a while loop indefinitely until the player says they no longer want to play by entering "n"

    while True:
        # get input and convert to lower case to prevent errors
        playAgain = input("\nWould you like to play (y/n)? ").lower()

        if playAgain == "y":
            # call game function and set counter and random number
            targetNumber = random.randint(1, 10)
            counter = 1
            play_game(targetNumber, counter)

        elif playAgain == "n":
            # exit function to end game
            print("Thanks for playing. Goodbye.")
            exit()

        else:
            print("Please enter a valid choice.")

display_title()
main()


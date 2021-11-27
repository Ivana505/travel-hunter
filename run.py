import random
import sys
import pyfiglet
cities = [
    'AMSTERDAM', 'ANDORRA LA VELLA', 'ATHENS', 'BELGRADE', 'BERLIN', 'BERN',
    'BRATISLAVA', 'BRUSSELS', 'BUCHAREST', 'BUDAPEST', 'CHISINAU',
    'COPENHAGEN', 'DUBLIN', 'HELSINKI', 'KIEV', 'LISBON', 'LJUBLJANA',
    'LUXEMBOURG', 'MADRID', 'MINSK', 'MONACO', 'OSLO', 'PARIS', 'PODGORICA',
    'PRAGUE', 'REYKJAVIK', 'RIGA', 'ROME', 'SAN MARINO', 'SARAJEVO', 'SKOPJE',
    'SOFIA', 'STOCKHOLM', 'TALLINN', 'TIRANA', 'VADUZ', 'VALLETTA', 'VIENNA',
    'VILNIUS', 'WARSAW', 'ZAGREB']
countries = [
    'ALBANIA', 'ANDORRA', 'AUSTRIA', 'BELARUS', 'BELGIUM',
    'BOSNIA AND HERZEGOVINA', 'BULGARIA', 'CROATIA', 'CZECHIA',
    'DENMARK', 'ESTONIA', 'FINLAND', 'FRANCE', 'GERMANY', 'GREECE',
    'HOLY SEE', 'HUNGARY', 'ICELAND', 'IRELAND', 'ITALY', 'KOSOVO',
    'LATVIA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MALTA',
    'MOLDOVA', 'MONACO', 'MONTENEGRO', 'NETHERLANDS', 'NORTH MACEDONIA',
    'NORWAY', 'POLAND', 'PORTUGAL', 'ROMANIA', 'SAN MARINO', 'SERBIA',
    'SLOVAKIA', 'SLOVENIA', 'SPAIN', 'SWEDEN', 'SWITZERLAND', 'UKRAINE']


def start_game():
    """
   Starts game and calls welcome message function
   first and then choose game function for the
   player to choose type of the game.
    """
    welcome_message()
    choose_game()


def welcome_message():
    """
   Welcome message function with explanation
   how the game is played.
    """
    print(pyfiglet.figlet_format("Welcome to travel hunter", justify="center"))
    while True:
        name = input("What is your name?\n")
        if name.isalpha():
            print(f"Good day {name} !")
            print("Try to guess the hidden word to get to your destination.")
            print("You have 8 tries.")
            choose_game()
        else:
            print("I do not understand, add letters only.\n")
            welcome_message()


def choose_game():
    """
   Gives an option to choose between two type of games.
   Isalpha is making sure player chooses letter.
   Else statement is making sure game does not start
   until correct letter has been chose either G or Z.
    """
    print("Choose a category.")
    game_choice = input(
        "European cities (press G) or European countries (press Z).\n").upper()
    if game_choice.isalpha() and game_choice == 'G':
        chosen_city = get_random(cities)
        play_game(chosen_city)

    elif game_choice.isalpha() and game_choice == 'Z':
        chosen_country = get_random(countries)
        play_game(chosen_country)
    else:
        print("I do not understand, please add letter only.")
    choose_game()


def enter_check():
    """
   While true loop is making sure only one single character,
   in this case letter has been chosen by the player.
    """
    input_char = input("Enter single character: ")

    while True:
        if (input_char.lower() in "abcdefghijklmnopqrstuvwxyz"
           and len(input_char) == 1):
            break

        input_char = input("Enter single character: ")

    return input_char


def get_random(word):
    """
    Function which returns the random
    word from the array.
    """
    rand_word = random.choice(word)
    return rand_word


def play_game(rand_word):
    """
    Main function of the game which scans if the letter that is in
    the random word is guessed or not. If guessed letter will show
    if not guessed attempts will reduce by 1. If the word is
    guessed player wins, if not word is revealed. In both scenarios
    player is passed to game end function.
    """
    attempts = 8
    guessed_letters = []
    done = False
    while not done:
        for letter in rand_word:
            if letter.upper() in guessed_letters:
                print(letter, end=" ")
            else:
                print("_ ", end=" ")
        print("")
        print(f"\nAmount of the attempts left {attempts}, Next Guess \n")
        guess = enter_check()
        guessed_letters.append(guess.upper())

        if guess.isalpha() and guess.upper() not in rand_word.upper():
            attempts -= 1
            if attempts == 0:
                done = True
                print(f"The secret word was: {rand_word.upper()}")
                game_end()
                break

        done = True
        for letter in rand_word:
            if letter.upper() not in guessed_letters:
                done = False

        if done:
            print(f"You guessed secret word, it is: {rand_word.upper()}")
            print("YOU WIN !")
            game_end()


def game_end():
    """
    Asks if player wants to continue playing the game or not.
    After Y or N message is displayed.
    """
    again = input("Do you want to play again press Y or N ?\n").upper()
    if again == 'Y':
        print(" Yes is a good answer, enjoy playing again ! ")
        choose_game()
    elif again == 'N':
        print("Oh no ! You are leaving, I hope to see you again soon ! \n")
        goodbye_message()
    else:
        print("I do not understand, please try again. Press Y or N.")
        game_end()


def goodbye_message():
    """
   Final function which ends the game if the
   player pressed N to end the game.
   It also prints Goodbye message with pyfiglet.
    """
    print(pyfiglet.figlet_format("Goodbye ! ", justify="center"))
    sys.exit()


start_game()

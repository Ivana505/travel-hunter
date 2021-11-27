import pyfiglet
import random
import sys
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
    welcome_message()
    choose_game()


def welcome_message():
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


	# def enter_check():
	# 		if (len(guessed_letters) != 1) or (letter not in guessed_letters):
	# 			raise ValueError("Only a single letter is allowed")

# def enter_check():
#     if len(guess) != 1:
#         print('Please enter a single letter.')
#     elif guess in guessed_letters:
#         print('You have already guessed that letter. Choose again.')
    


def get_random(word):
    rand_word = random.choice(word)
    return rand_word


def play_game(rand_word):
    attempts = 8
    guessed_letters = []
    done = False
    while not done:
        for letter in rand_word:
	              #enter_check()
            if letter.upper() in guessed_letters:
                print(letter, end=" ")
            else:
                    print("_ ", end=" ")
        print("")
        guess = input(f"\nAmount of the attempts left {attempts}, Next Guess: ")
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
    print(pyfiglet.figlet_format("Goodbye ! ", justify="center"))
    sys.exit()


start_game()

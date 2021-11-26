import pyfiglet
import random
import sys
cities = [
    'ZAGREB', 'DUBLIN', 'AMSTERDAM', 'MADRID', 'FRANKFURT',
    'ROTTERDAM', 'REYKJAVIK', 'BUDAPEST', 'ATHENS', 'CHISINAU']
countries = [
    'CROATIA', 'NETHERLANDS', 'IRELAND', 'GERMANY', 'POLAND',
'SLOVAKIA', 'MALTA', 'SWEDEN', 'GREECE', 'FRANCE']


def start_game():
	welcome_message()
	choose_game()


def welcome_message():
	print(pyfiglet.figlet_format("Welcome to travel hunter", justify="center"))
	while True:
		name = input("What is your name?\n")
		if name.isalpha():
			print(f"Good day {name} ! Try to guess the hidden word to get to your destination. You have 8 tries.")
			choose_game()
		else:
			print("I do not understand, add letters only.\n")
			welcome_message()

	
def choose_game():
	game_choice = input("Choose a category: European cities (press G) or European countries (press Z).\n").upper()
	if game_choice == 'G':
		chosen_city = get_random(cities)
		play_game(chosen_city)

	elif game_choice == 'Z':
		chosen_country = get_random(countries)
		play_game(chosen_country)
	else:
		print("I do not understand, please try again. Press G or Z.")
	choose_game()


def get_random(word):
	rand_word = random.choice(word)
	return rand_word


def play_game(rand_word):
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
		guess = input(f"Amount of the attempts left {attempts}, Next Guess: ")
		guessed_letters.append(guess.upper())

		if guess.upper() not in rand_word.upper():
				attempts -= 1
				if attempts == 0:   
					done = True
					print("The secret word was: "+ rand_word.upper())
					game_end()
					break
		
		done = True
		for letter in rand_word:
			if letter.upper() not in guessed_letters:
				done = False
		
		if done:
			print("You guessed secret word, it is: "+ rand_word.upper())
			print ("YOU WIN !")
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






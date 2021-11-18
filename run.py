import random
cities = [
	'Zagreb', 'Dublin', 'Amsterdam', 'Madrid', 'Frankfurt',
	'Rotterdam', 'Reykjavik', 'Budapest', 'Athens', 'Chisinau']
countries = [
	'Croatia', 'Netherlands', 'Ireland', 'Germany', 'Poland',
	'Slovakia', 'Malta', 'Sweeden', 'Greece', 'France']


def get_random(word):
	rand_word = random.choice(word)
	print("_ " * len(rand_word))
	


def welcome_message(player):
	print(f"Good day {player} ! Try to guess the hidden word to get to your destination.")


name = input("What is your name?\n")
welcome_message(name)
choose_game = input('Choose a category: European cities (press G) or European countries (press Z).\n')

if choose_game.upper() == 'G':
	get_random(cities)
elif choose_game.upper() == 'Z':
	get_random(countries)


def play_game(guess):
	guessing = input("Enter letter: \n")
	letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	while letter in random_word:
		print("You guessed the letter, guess again !")
	else:
		print("Try again !")
#while letter in rand_word:
	print("Great, keep guessing")
#if letter not in rand_word:
#	break
	#print("Try again")

	


# def end_game

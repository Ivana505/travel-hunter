import random
cities = [
	'Zagreb', 'Dublin', 'Amsterdam', 'Madrid', 'Frankfurt',
	'Rotterdam', 'Reykjavik', 'Budapest', 'Athens', 'Chisinau']
countries = [
	'Croatia', 'Netherlands', 'Ireland', 'Germany', 'Poland',
	'Slovakia', 'Malta', 'Sweeden', 'Greece', 'France']

score = 8


def start_game():
	welcome_message()
	choose_game()


def welcome_message():
	name = input("What is your name?\n")
	print(f"Good day {name} ! Try to guess the hidden word to get to your destination.")

def choose_game():
	game_choice = input('Choose a category: European cities (press G) or European countries (press Z).\n').upper()
	if game_choice == 'G':
		chosen_city = get_random(cities)
		play_game(chosen_city)
	elif game_choice == 'Z':
		chosen_country = get_random(countries)
		play_game(chosen_country)


def get_random(word):
	rand_word = random.choice(word)
	#print("_ " * len(rand_word))
	return rand_word


def play_game(word):
	print(word)
	letter = []
	board = ''
	for character in word:
		board += '_ '
	print(board)
	while True:
		guessing = input("Enter letter: \n").upper()
		if guessing in word:
			print("Good guess")
			board[board.index(guessing)] = guessing
			print(board)
			break
		else:
			print("Try again !")
			continue
	    





start_game()








#while letter in rand_word:
	#print("Great, keep guessing")
#if letter not in rand_word:
#	break
	#print("Try again")

	
# def end_game

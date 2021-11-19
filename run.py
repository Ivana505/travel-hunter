import random
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
	name = input("What is your name?\n")
	print(f"Good day {name} ! Try to guess the hidden word to get to your destination. You have 8 tries. ")


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
		print(" ")
			
	guess = input(f"Amount of the attempts left {attempts}, Next Guess: ")
	guessed_letters.append(guess.upper())
	if guess.upper() not in rand_word.upper():
		attempts -=1
		if attempts == 0:
			done = True
	for letter in rand_word:
		 if letter.upper() not in guessed_letters:
			 done = False

	if done:
		print("well done")
	else:
		print("you lost!")
 

start_game()






#check_guess():


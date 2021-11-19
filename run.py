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
	print("_ " * len(rand_word))
	return rand_word


def play_game(word):
	print(word)
	print("This word is", len(word), "letters long.")
	while True:
		guessing = input("Guess a letter: \n").upper()
		if guessing in word:
			print("Good guess")
			get_guess()
			game_end()
			break
		else:
			print("Try again !")
			continue


def get_guess():
	points = 8
	guessed = ''
	valid_entry =set('abcdefghijklmnopqrstuvwz')
	while len(word) > 0:
		rand_word = ""
		missed = 0

	for letter in word:
		if leter in guessed:
			rand_word = rand_word + letter
		else:
			rand_word = rand_word + "_ "
			get_guess()



def game_end():
	guessed = True
	while guessed:
		print = input("Would you like to continue playing the game? y/n ")
		if start_game() == "y":
			print("You have decided to continue playing the game.")
		elif start_game() == "n":
			print("Now closing the game...")
			guessed = False
		else:
			print("That is not a valid option. Please try again.")
			print("Thanks for playing")

	

	



	




start_game()






#check_guess():


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
	print(rand_word)


def welcome_message(pizza):
	print(f"Good day {pizza} ! Try to guess the hidden word to get to your destination.")


name = input("What is your name?\n")
welcome_message(name)
choose_game = input('Choose a category: European cities (press G) or European countries (press Z).\n')

if choose_game.upper() == 'G':
	get_random(cities)
	# print.random (cities)
	# str.replace = ("_ " * len(cities))
	# remove_letters = cities.replace('', '_')
elif choose_game.upper() == 'Z':
	get_random(countries)


# def start_game():
	# str.replace("cities", "_" ) 
	# str.replace("countries", "_") 
	# underscore = ("_ " * len(cities))

	# start_game()

# def guessing_letters()


# def end_game

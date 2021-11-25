import pyfiglet
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
	print(pyfiglet.figlet_format("Welcome to travel hunter", justify="center"))
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
	else:
		print("I do not understand, please try again. Press G or Z.")
	welcome_message()


def get_random(word):
	rand_word = random.choice(word)
	return rand_word


def play_game(rand_word):
	attempts = 8
	#letters_remaining = 0
	guessed_letters = []

	#word_completion = "_" * len(rand_word)
	#joinedList = ''.join(guessed_letters)
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

		# if len(used_letters) == len(rand_word):   
		#    attempts != 0
		#    if attempts != 0:
		# 	   done = True
		# 	   print('Yes! The secret word is"' + rand_word +'"! You have won!')
		# 	   break

		if guess.upper() not in rand_word.upper():
				attempts -= 1
				if attempts == 0:   
					done = True
					print("The secret word was: "+ rand_word.upper())
					break
		
		done = True
		for letter in rand_word:
			if letter.upper() not in guessed_letters:
				done = False
	if done:
		print ("you iwn")
	else:
		print("game over")
                    

	

			# if world_completion:
			# 	done = False
			# 	print('Yes! The secret word is "' + rand_word +'"! You have won!')
			# if len(rand_word) == len(guessed_letters):
			#    print('\nYou won the Game!')
			#    break
				

			# elif word_completion() == rand_word.upper():
			# 	 print("Yay! you won.")
			# 	 break


			# if len(guessed_letters) == len(rand_word):
			# 	guessed_letters == rand_word
			# 	done = True
			# 	print("you win")

			# if joinedList.upper() == rand_wordupper():
            #     print("Yay! you won.")
            #     break
            # elif attempts == 0:
            #     print("Too many Guesses!, Sorry better luck next time.")
				
			#if joinedList.upper() == rand_word.upper():
			#	done = True
			#	print("Yay! you won.")
				#break
			
			#if guessed = True:
			#	word_completion = rand_word
			#	print("well done")
			#	break

		#if guess.upper() in rand_word.upper():
		#	word_completion = rand_word
		#	done = True
			#print("you win")
		#	break
				
			
		#else:
			#letters_remaining -= 1
		#print(letters_remaining)
		#if letters_remaining == 0:
		#	done = True

	#if done:
	#	print("You lost ! ")
	#else:
		#print("You won ! ")
		
start_game()


# def game_end():
#    guessed = True
#    while guessed:
#        print = input("Would you like to continue playing the game? y/n ")
#        if start_game() == "y":
#            print("You have decided to continue playing the game.")
#        elif start_game() == "n":
#            print("Now closing the game...")
#            guessed = False
#         else:
#            print("That is not a valid option. Please try again.")
#            print("Thanks for playing")

#check_guess():


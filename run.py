def welcome_message():
    print("Good day player ! Try to guess the hidden word to get to your destination.")
welcome_message()
choose_game = input ('Choose a category: European cities (press G) or European countries (press Z).')
if choose_game.upper() == 'G':
      # print.random (cities)
       import random
       cities = ['Zagreb','Dublin','Amsterdam','Madrid','Frankfurt','Rotterdam','Reykjavik','Budapest','Athens','Chisinau']
       #str.replace = ("_ " * len(cities))
       #remove_letters = cities.replace('', '_')
       print(random.choice(cities))
      


elif choose_game.upper() == 'Z':
       import random
       countries = ['Croatia','Netherlands','Ireland','Germany','Poland','Slovakia','Malta','Sweeden','Greece','France']
       print(random.choice(countries))


#def start_game():
   # str.replace("cities", "_" ) 
  #  str.replace("countries", "_") 
   # underscore = ("_ " * len(cities))

  #  start_game()

#def guessing_letters()


#def end_game
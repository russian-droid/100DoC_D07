#following Udemy course: 100 days of code by Angela Yu

import random

print('\033c')
print('\n\n-------------------HANGMAN game-- --------------')
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')
#hamgman hangman_pics
stages = ["  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========",#6

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",#5

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",#4

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",#3

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",#2

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",#1

        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n========="]#0
#Word bank of animals
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

#state of the game, so we can change it in main loop later when it's over
game_is_finished = False
#list with hangman progression pics
lives = len(stages) - 1

#pick a random word (original word) from words list
chosen_word = random.choice(word_list)
#how many letters in it
word_length = len(chosen_word)

#new empty array, created to keep truck of user_guessed letters in the word
the_word_array = []
#to keep track of entered letters
tried_letters = []
#fill up that empty list, go via range of letters
for _ in range(word_length):
    #add an underscore into the list for each letter
    the_word_array += "_"

#main loop: it keeps runing until this condition changes
while not game_is_finished:
    #prompt for a letter
    user_guess = input("Guess a letter: \n").lower()

    #Use this to clear screen between user_guesses----------------------------------------------
    print('\033c')

    #go via the word, check if that letter the same letter entered again
    if user_guess in tried_letters:
        #don't penalize, just let them know
        print(f"Hey! You've already tried letter _{user_guess}_")
        print(f"Don't waste you tries. You've, in addition, tried letters: {' '.join(tried_letters)}\n")
    #after checking, safe this letter for the next time
    tried_letters.append(user_guess)
    

    #encorage user for a correct guess
    if user_guess in chosen_word and not the_word_array:
        print('YES, you assumed correctly')

    #go via the original word in range
    for position in range(word_length):
        #setting a variable 'letter' to keep the position of a known letter in the original word 
        letter = chosen_word[position]
        #if the letter that user entered same as a letter from the original word
        if letter == user_guess:
            #setting that letter to be at that position in word array
            the_word_array[position] = letter    
    #print out the word array
    print(f"{' '.join(the_word_array)}\n")

    #bad guess - penalize them
    #look for that letter in 
    if user_guess not in chosen_word:
        print(f"NOPE, letter _{user_guess}_ is not there :(")
        #delete one more life
        lives -= 1
        #when no more life, game ends
        if lives == 0:
            #to break the main loop
            game_is_finished = True
            print("No more tries buddy. You LOST!")
    
    #if all the letters are guessed, game ends
    if not "_" in the_word_array:
        #breaks main loop
        game_is_finished = True
        print("You WON!")

    print(stages[lives])

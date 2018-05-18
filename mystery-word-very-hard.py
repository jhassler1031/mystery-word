
#connect to functions in separate file

from mys_word_functions_very_hard import *

#The computer needs to choose a word at random after player chooses difficulty

with open("/usr/share/dict/words") as infile:
    words_list = infile.read()

words_list = words_list.split()


#Create different list per difficulty

easy_list = []
normal_list = []
hard_list = []
word_score = 0

for item in words_list:
    word_score = det_word_diff(item)
    if word_score > 4 and word_score < 12:
        easy_list.append(item)
    elif word_score > 12 and word_score < 18:
        normal_list.append(item)
    elif len(item) > 18:
        hard_list.append(item)

rand_word = choose_difficulty(easy_list, normal_list, hard_list)

#Now we have a random word.  Need to create the display word

word_length = len(rand_word)
miss_count = 8
correct_letters = []
incorrect_letters = []
wants_to_play = True


#Start user interface

print("Game Start:  The word is " + str(word_length) + " letters long.  Good luck!")

while wants_to_play:
    while True:
        print("You have " + str(miss_count) + " misses remaining.")
        print(display_word(correct_letters, rand_word))
        correct_letters, incorrect_letters, miss_count = player_turn(rand_word, correct_letters, incorrect_letters, miss_count)
        print(hangman(miss_count))

        if rand_word == display_word(correct_letters, rand_word):
            print("Congratulations!  You've won!")
            print("The word was " + rand_word + ".")
            break
        elif miss_count <= 0:
            print("I'm sorry, you've lost.")
            print("The word was " + rand_word + ".")
            break
        else:
            print("Next turn.")
    answer = input("Would you like to play again? Y or N: ")
    if answer.lower() == "y":
        miss_count = 8
        correct_letters = []
        incorrect_letters = []
        rand_word = choose_difficulty(easy_list, normal_list, hard_list)
    else:
        wants_to_play = False

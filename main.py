#Step 2
#### BREAKS DOWN LOGIC STRARTING AT 7 MINS
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#Solution 1 for loop for in
# display = []
# for letter in chosen_word:
#   display += "_"
# print(display)

####for in range solution
display = []
## created a variable of word length since using it so much
word_length = len(chosen_word)

for _ in range (len(chosen_word)):
  display += "_"
print(display)

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#We have to change the code because we have to get the letter in the position 

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

## SO WE WILL HAVE TO CHANGE IT TO THIS BELOW
# each time it loops it will give us a postion a number to work with, first time it runs it position will be equal to 0, then 1, 

for position in range(word_length):
    letter = chosen_word[position]
    #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
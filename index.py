import random
from word_box import words
from life_stage import lives
# Welcome Message
print('HANGMAN GAME!!!')
# Picking words
chosen_word = random.choice(words)
# Checking word lenght
word_len = len(chosen_word)
# Providing hint for the user
if word_len > 5:
    print(f'hints: {chosen_word[0]} {chosen_word[1]} {chosen_word[-1]}')
else:
    print(f'hints: {chosen_word[0]}')
display = []
life_bar = 6
game_end = False
for space in range(word_len):
    display+= '_'
print(display)
while not game_end:
    guess = input('Enter an alphabeth ').lower()        
    for postion in range(word_len):
        letter = chosen_word[postion]
        if letter == guess:
            display[postion] = guess
    print(display)
    
    if guess not in chosen_word:
        life_bar -= 1
        print('Wrong guess')
        if life_bar == 0:
            game_end = True
            print('You have lost')
    
    if '_' not in display:
        game_end = True
        print("You have won")

    print(lives[life_bar])
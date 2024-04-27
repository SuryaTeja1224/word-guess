#Guessing a random word
import random
import time
def word_guess(attempts, chosen_word, li,hints):
    while attempts > 0 and '_' in li:
        print(' '.join(li) + '\n')
        guess = input("Guess the word ").lower().strip()
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    li[index] = guess
        else:
            print("Guess Again!........ Noob")
            ask = input("Bro....Try to take hint").strip().upper()
            if ask[0] == 'Y':
                for key in hints:
                    if key[0] == chosen_word:
                        print(key[1][0])
                        as1 = input("Can you guess now (Y/N)?").upper().strip()
                        if as1[0] == 'Y':
                            word_guess(attempts, chosen_word, li, hints)
                        elif as1[0] == 'N':
                            print(key[1][1])
                            attempts -= 1
            elif (ask[0] == 'N'):
                pass
    if '_' not in li:
        print("You've guessed the word")
        print(''.join(li).capitalize())
    elif(attempts == 0):
        print("You're Out of your attempts")
        time.sleep(3)
        print("Noobbbbbbbbb")
        time.sleep(2)
        print(f"Correct word is {(chosen_word).capitalize()}")

print("Welcome to word Guess")
words = ['everest', 'kailash', 'python', 'escape']
hints = [['everest',['Related to mountains..', 'Largest Peak']],['kailash', ['Related to mountains..', 'Most Powerful Place']],['python',['Your Most Fav programming language', 'On what future is based']],['escape', ['What you wanna do if you are in danger!!', 'run away or....?']]]
attempts = 6
chosen_word = random.choice(words)
li = ['_' for _ in chosen_word]
print(f"{' '.join(li)} Ummm.. a {len(chosen_word)} letter word may bee...")
assist = input("You need help on guessing?..(Y?N) ").upper().strip()
if (assist[0] == 'Y'):
    for key in hints:
        if key[0] == chosen_word:
            print(key[1][0])
            as1 = input("Can you guess now (Y/N)?").upper().strip()
            if as1[0] == 'Y':
                word_guess(attempts, chosen_word, li, hints)
            elif as1[0] == 'N':
                print(key[1][1])
                word_guess(attempts, chosen_word, li,hints)
elif (assist[0] == 'N'):
    word_guess(attempts, chosen_word, li,hints)
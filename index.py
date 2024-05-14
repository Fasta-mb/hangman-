import random

wordList = ["ardvark", "baboon", "camel", "dog", "cat", "cheese", "coffee"]

chosenWord = random.choice(wordList)
print(chosenWord)

display = []
game_on = True
lives = 6


# fill the display array with underscore by the chosenWord lenght
for _ in range(len(chosenWord)):
    display += ("_")
print(display)

while game_on:

    guess = input("guess a letter:\n").lower()

    for i in range(len(display)):
        if chosenWord[i] == guess:
            display[i] = guess
        
        
    print(display)
  # if the word the user guess is not in the chosen word, the user live will reduce by 1
    if guess not in chosenWord:
        lives -= 1
        if lives == 0:
            print("you lose")
            game_on = False
            
    print(f"live remaining {lives}")
    # if the user guess the word, the user win
    if "_" not in display:
        print("you win")
        game_on = False

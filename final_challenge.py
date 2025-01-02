import json
import random

def treasure_room():

    with open('TRClues.json', 'r') as f:
        data = json.load(f)
        tv_game = data['Fort Boyard']

    available_years = list(tv_game.keys())
    year = random.choice(available_years)
    programs = list(tv_game[year].keys())
    game = random.choice(programs)

    clues = tv_game[year][game]['Clues']
    code_word = tv_game[year][game]["CODE-WORD"]

    for i in range(min(3, len(clues))):
        print(clues[i])


    attempts = 0
    answer_correct = False

    while attempts < 3 and not answer_correct:
        answer = str(input("Enter the code word: ")).upper()
        attempts += 1

        if answer == code_word:
            answer_correct = True
        else:
            remaining_attempts = 3 - attempts
            if remaining_attempts > 0:
                print(f"Incorrect. You have {remaining_attempts} attempts remaining.")

                if attempts < len(clues):
                    print("Here's another clue:", clues[attempts])
            else:
                print("Incorrect. The code word was:", code_word)

    if answer_correct:
        print("Congratulations! You have opened the treasure room!")
    else:
        print("You failed to open the treasure room.")

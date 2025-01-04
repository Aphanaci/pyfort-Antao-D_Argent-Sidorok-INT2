import json
import random

## Put the content of a json in a dictionary
def load_riddles(file):
    f = open(file, 'r')
    data = json.load(f)
    f.close()
    return data

## Use the previous function to read a json containing riddles that the player has to solve
def pere_fouras_riddles():
    attempts = 3
    l = load_riddles('PFRiddles.json')
    riddle = random.choice(l)
    print(riddle.get('question'))
    while attempts > 0:
        player_answer = str(input())
        player_answer = player_answer.lower()
        answer = riddle.get('answer')
        if player_answer == answer.lower():
            print('Correct! You win a key.')
            return True
        else:
            attempts -= 1
            if attempts > 0 :
                print(f'This answer is incorrect. You have {attempts} attempts remaining.')
            else :
                print("You don't have attempts left. The correct answer was: " + answer)
                return False
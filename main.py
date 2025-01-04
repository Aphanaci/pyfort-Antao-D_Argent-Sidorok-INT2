from math_challenges import *
from chance_challenges import *
from logic_challenges import *
from pere_fouras_challenge import *
from final_challenge import *
from utility_functions import *

## Making the structure of the game
def game():
    introduction()
    print("Now let's make your team!")
    team = compose_team()
    keys = 0
    while keys < 3 :
        chall_choice = challenges_menu()
        player = choose_player(team)
        if chall_choice == 1 :
            win = math_challenge()
            if win :
                keys += 1
                player['keys_wons']+=1
        elif chall_choice == 2 :
            win = battleship_game()
            if win:
                keys += 1
                player['keys_wons'] += 1
        elif chall_choice == 3 :
            win = chance_challenge()
            if win:
                keys += 1
                player['keys_wons'] += 1
        elif chall_choice == 4 :
            win = pere_fouras_riddles()
            if win:
                keys += 1
                player['keys_wons'] += 1
    print("You have now access to the last challenge: the treasure room !\n")
    print("The rules are simple, you're gonna have 3 clues at the start, corresponding to a word.\n")
    print("For each failed attempt, you will have one more clue up until 6 clues.\n")
    print("Be careful, if you fail after three attempts, you lose...\n")
    treasure_room()
    print(team)

game()
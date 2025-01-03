from math_challenges import *
from chance_challenges import *
from logic_challenges import *
from pere_fouras_challenge import *
from final_challenge import *
from utility_functions import *

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
    treasure_room()
    print(team)

game()
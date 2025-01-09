import random

## Shell game where you have to find a key randomly placed under one of the three shells proposed
def shell_game():

    l = ['A', 'B', 'C']
    attempts = 2
    print(f"Welcome to the shell game ! You're going to have 3 shells in front of you, and you must choose one of them. Under one of them is where the key is hiding, and you have {attempts} attempts to find it. \n The choices are A, B or C.")


    while attempts > 0:

        stash = random.choice(l)
        print(f"You have {attempts} attempts remaining")
        choice = str(input("Which shell do you choose?"))
        choice = choice.upper()

        if choice not in l:
            print("The shell you choosed does not exist.")

        elif choice == stash:
            print(f"You have found the good shell ! You win a key.")
            return True

        elif attempts > 1 and choice != stash :
            print("You didn't choose the good shell...")

        attempts -= 1

    print(f"You didn't choose the good shell and spent all of your attempts to find it. The key was under the shell {stash}")
    return False


## Game of rolling dices where the goal is to get a six, if no one gets it, it's a draw
def roll_dice_game():

  max_attempts = 3

  for attempt in range(1, max_attempts + 1):
    print(f"Attempt {attempt}/{max_attempts}")
    input("Press Enter to roll the dice")

    player_dice = (random.randint(1, 6), random.randint(1, 6))
    print(f"You rolled: {player_dice}")

    if 6 in player_dice:
      print("You win! The key is yours.")
      return True

    game_master_dice = (random.randint(1, 6), random.randint(1, 6))
    print(f"Game master rolled: {game_master_dice}")

    if 6 in game_master_dice:
      print("Game master wins!")
      return False

    print("No 6 rolled...")

  print("No player scored a 6 after three tries. It's a draw.")
  return False

## Select a random chance challenge
def chance_challenge():
    challenges = [shell_game, roll_dice_game]
    challenge = random.choice(challenges)
    return challenge()
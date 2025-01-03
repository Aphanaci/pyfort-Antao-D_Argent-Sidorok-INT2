def introduction():
    print("\nWelcome to Fort Boyard!\n")
    print("Prepare for an adventure filled with challenges and puzzles.")
    print("Your goal is to collect three keys to unlock the treasure room.\n")
    print("Here's how it works:")
    print("- You'll face a series of challenges.")
    print("- Completing each challenge successfully earns you a key.")
    print("- Once you've collected all three keys, you can enter the treasure room.")
    print("- In the treasure room, you'll need to decipher a code to claim the treasure.\n")
    print("Good luck!\n")



def compose_team():

    while True:
        try:
            num_players = int(input("Enter the number of players (up to 3): "))
            if 1 <= num_players <= 3:
                break
            else:
                print("Error: The number of players must be between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    team = []
    leader_assigned = False

    for i in range(num_players):
        player = {}
        player["name"] = input(f"Enter the name of player {i + 1}: ")
        player["profession"] = input(f"Enter the profession of player {i + 1}: ")

        if not leader_assigned:
            while True:
                is_leader = input(f"Is {player['name']} the team leader? (yes/no): ").lower()
                if is_leader in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            player["leader"] = (is_leader == "yes")
            if player["leader"]:
                leader_assigned = True
        else:
            player["leader"] = False

        player["keys_wons"] = 0
        team.append(player)

    if not leader_assigned and team:
        team[0]["leader"] = True
        print(f"{team[0]['name']} has been automatically assigned as team leader.")

    return team



def challenges_menu():

    while True:
        print("\nChoose your challenge:")
        print("1. Mathematics challenge")
        print("2. Logic challenge")
        print("3. Chance challenge")
        print("4. Père Fouras riddle")

        try:
            choice = int(input("Enter the number of your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")



def choose_player(team):

    print("\nTeam Roster:")
    for i, player in enumerate(team):
        role = "Leader" if player["leader"] else "Member"
        print(f"{i + 1}. {player['name']} ({player['profession']}) - {role}")

    while True:
        try:
            player_number = int(input("Enter the player's number: "))
            if 1 <= player_number <= len(team):
                return team[player_number - 1]
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(team)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
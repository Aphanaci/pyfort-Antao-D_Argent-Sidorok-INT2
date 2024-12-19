import random

##Game of NIM
def display_sticks(n):
    print("Remaining sticks:", n* "|")

def player_removal(n):
    a = int(input("How many sticks do you want to remove (1, 2, or 3)?"))
    while a not in [1,2,3] and a<n:
        a = int(input("You can't remove this amount of sticks. How many sticks do you want to remove (1, 2, or 3)?"))
    return a

def master_removal(n):
    a = n%4
    return a

def nim_game():
    n = 20
    players_turn = True
    while n > 0:
        display_sticks(n)
        for _ in range(2):
            if players_turn:
                n = n - player_removal(n)
                players_turn = False
            else:
                n = n - master_removal(n)
                players_turn = True
    if players_turn:
        print("The game master removed the last stick. The player wins!")
        return True
    else:
        print("The player removed the last stick. The game master wins...")
        return False


##Battleship game
def next_player(player):
    return 1 - player

def empty_grid():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_grid(grid, message):
    print(message)
    print("  +---+---+---+")
    for i, row in enumerate(grid):
        print(f"{i} | {' | '.join(row)} |")
        print("  +---+---+---+")
    print("    0   1   2  ")

def ask_position():
    while True:
        try:
            pos = input("Enter position (row,col): ")
            row, col = map(int, pos.split(','))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid position. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input format. Please enter as 'row,col'.")

def initialize():
    grid = empty_grid()
    for _ in range(2):
        while True:
            display_grid(grid, "Place your boats:")
            row, col = ask_position()
            if grid[row][col] == " ":
                grid[row][col] = "B"
                break
            else:
                print("Position already occupied.")
    return grid

def turn(player, player_shots_grid, opponent_grid):
    print(f"\nPlayer {player}'s turn:")
    display_grid(player_shots_grid, "Your shots:")

    if player == 0:
        row, col = ask_position()
        while player_shots_grid[row][col] != " ":
            print("You've already shot there. Try again.")
            row, col = ask_position()
    else:
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if player_shots_grid[row][col] == " ":
                break
        print(f"Game master shoots at {row},{col}")

    if opponent_grid[row][col] == "B":
        print("Hit!")
        player_shots_grid[row][col] = "X"
        opponent_grid[row][col] = "X"
    else:
        print("Miss.")
        player_shots_grid[row][col] = "."
        opponent_grid[row][col] = "."


def has_won(player_shots_grid):
    hit_count = sum(row.count("X") for row in player_shots_grid)
    return hit_count == 4

def battleship_game():
    print("Welcome to Battleship!")
    print("Each player must place 2 boats on a 3x3 grid.")

    player_grid = initialize()
    print("\nYour boats are placed:")
    display_grid(player_grid, "Your boats:")

    game_master_grid = empty_grid()
    boat_count = 0
    while boat_count < 2:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if game_master_grid[row][col] == " ":
            game_master_grid[row][col] = "B"
            boat_count += 1

    player_shots_grid = empty_grid()
    game_master_shots_grid = empty_grid()

    current_player = 0

    while True:
        turn(current_player, player_shots_grid if current_player == 0 else game_master_shots_grid,
             game_master_grid if current_player == 0 else player_grid)

        if has_won(player_shots_grid if current_player == 0 else game_master_shots_grid):
            print(f"\nPlayer {current_player} wins!")
            return True if current_player == 0 else False

        current_player = next_player(current_player)
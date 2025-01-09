import random

## Go to the next player
def next_player(player):
    return 1 - player

## Create a grid to play
def empty_grid():
    return [[" " for _ in range(3)] for _ in range(3)]

## Display the grid created
def display_grid(grid, message):
    print(message)
    print("  +---+---+---+")
    for i, row in enumerate(grid):
        print(f"{i} | {' | '.join(row)} |")
        print("  +---+---+---+")
    print("    0   1   2  ")

## Register the position of the boats wanted by the user
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

## Put the boats where the user wants
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

## Decide the turn of the player
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

## Verify if there is a winner
def has_won(player_shots_grid):
    hit_count = sum(row.count("X") for row in player_shots_grid)
    return hit_count == 2

## Launching and playing the battleship game
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
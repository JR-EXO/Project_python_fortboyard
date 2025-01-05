import random


# Function to display a specified number of sticks
def display_sticks(n):
    for i in range(n):
        print("|")

# Function to handle player's stick removal action
def player_removal(n):
    sticks = int(input("There are %d sticks left. How many will you remove? (1, 2, or 3) " % n))
    while sticks < 1 or sticks > 3 or sticks > n:
        sticks = int(input("Invalid input. Please enter a valid number of sticks: "))
    return sticks

# Function to determine the master's stick removal strategy
def master_removal(n):
    strategy = n % 4
    if strategy == 0:
        return 3
    elif strategy == 1:
        return 2
    elif strategy == 2:
        return 1
    elif strategy == 3:
        return 3


def nim_game():
    sticks = 20
    player_turn = True
    while sticks > 0:
        display_sticks(sticks)
        if player_turn:
            sticks -= player_removal(sticks)
        else:
            sticks -= master_removal(sticks)
        print("Sticks left: %d" % sticks)
        player_turn = not player_turn
    print("Game over. You win!" if not player_turn else "Game over. You lose!")
    return not player_turn

def display_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 5)

def check_victory(grid, symbol):
    for row in grid:
        if all(cell == symbol for cell in row):
            return True
    for col in range(len(grid[0])):
        if all(grid[row][col] == symbol for row in range(len(grid))):
            return True
    if all(grid[i][i] == symbol for i in range(len(grid))):
        return True
    if all(grid[i][len(grid)-i-1] == symbol for i in range(len(grid))):
        return True
    return False

def master_move(grid, symbol):
    opponent = "X" if symbol == "O" else "O"
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "":
                grid[row][col] = symbol
                if check_victory(grid, symbol):
                    return (row, col)
                grid[row][col] = ""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "":
                grid[row][col] = opponent
                if check_victory(grid, opponent):
                    return (row, col)
                grid[row][col] = ""
    row = random.randint(0, len(grid)-1)
    col = random.randint(0, len(grid[row])-1)
    while grid[row][col] != "":
        row = random.randint(0, len(grid)-1)
        col = random.randint(0, len(grid[row])-1)
    return (row, col)

def player_turn(grid):
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if grid[row][col] == "":
            grid[row][col] = "X"
            break
        else:
            print("This square is occupied. Please choose a different one.")

def master_turn(grid):
    row, col = master_move(grid, "O")
    grid[row][col] = "O"

def full_grid(grid):
    for row in grid:
        for cell in row:
            if cell == "":
                return False
    return True

def check_result(grid):
    if check_victory(grid, 'X'):
        print("Player 'X' wins!")
        return True
    if check_victory(grid, 'O'):
        print("Player 'O' wins!")
        return True
    if full_grid(grid):
        print("The game is a draw!")
        return True
    return False


def tictactoe_game():
    grid = [['' for _ in range(3)] for _ in range(3)]
    def display_grid():
        for row in grid:
            print(" | ".join(cell if cell != '' else ' ' for cell in row))
        print()
    print("Welcome to Tic-Tac-Toe!")
    display_grid()
    while True:
        print("Player 'X', it's your turn!")
        player_turn(grid)
        display_grid()
        if check_result(grid):
            return True
        print("Game master 'O', it's your turn!")
        master_turn(grid)
        display_grid()
        if check_result(grid):
            return False

def next_player(player):
    return 1 - player

def empty_grid2():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_grid2(grid2, message):
    print(message)
    for row in grid2:
        print("|".join(row))
        print("-" * 5)

def ask_position():
    while True:
        pos = input("Enter a position (row,column): ")
        row, col = map(int, pos.split(","))
        if 0 <= row < 3 and 0 <= col < 3:
            return row, col
        else:
            print("Invalid position. Please enter values between 0 and 2.")

def initialize():
    grid2 = empty_grid2()
    boats = 0
    while boats < 2:
        display_grid(grid2, "Place your boats on the grid:")
        row, col = ask_position()
        if grid2[row][col] == " ":
            grid2[row][col] = "B"
            boats += 1
        else:
            print("Position already occupied. Choose another spot.")
    return grid2

def turn(player, player_shots_grid2, opponent_grid2):
    display_grid2(player_shots_grid2, "Your shot history:")

    if player == 0:  # Human player
        row, col = ask_position()
    else:  # Game master
        row, col = random.randint(0, 2), random.randint(0, 2)
        print(f"Game master chooses position: {row},{col}")

    if opponent_grid2[row][col] == "B":
        print("Hit!")
        player_shots_grid2[row][col] = "x"
        opponent_grid2[row][col] = "x"
    else:
        print("Miss!")
        player_shots_grid2[row][col] = "."

def has_won(player_shots_grid):
    return sum(row.count("x") for row in player_shots_grid) == 2

def battleship_game():
    print("Welcome to the Battleship game adventurer!")
    print("Each player places 2 boats on a 3x3 grid. First to sink both boats wins.")
    player_grid2 = initialize()
    game_master_grid2 = empty_grid2()
    for _ in range(2):
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if game_master_grid2[row][col] == " ":
                game_master_grid2[row][col] = "B"
                break
    player_shots_grid2 = empty_grid2()
    game_master_shots_grid2 = empty_grid2()
    current_player = 0
    while True:
        if current_player == 0:
            print("\nPlayer's turn!")
            turn(0, player_shots_grid2, game_master_grid2)
            if has_won(player_shots_grid2):
                print("Congratulations! You sank all the game master's boats!")
                return True
        else:
            print("\nGame master's turn!")
            turn(1, game_master_shots_grid2, player_grid2)
            if has_won(game_master_shots_grid2):
                print("The game master sank all your boats! You lost.")
                return False

        current_player = next_player(current_player)

def logical_challenge():
    challenges = [tictactoe_game, battleship_game, nim_game]
    challenge = random.choice(challenges)
    return challenge()
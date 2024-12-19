import random


def display_sticks(n):
    for i in range(n):
        print("|")



def player_removal(n):
    sticks = int(input("There are %d sticks left. How many will you remove? (1, 2, or 3) " % n))
    while sticks < 1 or sticks > 3 or sticks > n:
        sticks = int(input("Invalid input. Please enter a valid number of sticks: "))
    return sticks

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
    
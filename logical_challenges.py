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
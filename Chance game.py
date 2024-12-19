import random
def shell_game():
    attempt = 0
    shells = ['A','B','C']
    print("Hello adventurer ! If you want to win a key, select the right shell and let it be.")
    print("You have 3 shells, shell A, shell B and shell C.")
    print("Under one of them the key is hidden.")
    print("You have 2 try to find it.")
    print("Good luck adventurer")
    key_shell = random.choice(shells)
    while attempt < 2:
        print(f"\nAttempt {attempt + 1} of 2.")
        player_choice = input("Choose a shell adventurer :").strip().upper()
        if player_choice in shells:
            if player_choice == key_shell:
                print(f"Congratulations! You found the key under shell {key_shell}!")
                return True
            else:
                print(f"Sorry, the key is not under shell {player_choice}.")
        else:
            print("Invalid choice. Please choose A, B, or C.")
        attempt += 1
    print("\nYou have failed adventurer.")
    print("No more attempt left.")
    print(f"The key was under shell {key_shell}. Better luck next time adventurer!")
    return False

def roll_dice_game():
    max_attempt = 3
    print("Welcome to the Rolling Dice Game adventurers!")
    print("The first to roll a 6 wins! You and the game master each have 3 attempts.\n")
    for attempt in range(1, max_attempt + 1):
        print(f"Attempt {attempt} of {max_attempt}:")
        input("Press Enter to roll the dice...")
        player_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"You rolled: {player_dice}")
        if 6 in player_dice:
                print("Congratulations! You rolled a 6 and won the game!")
                return
        game_master_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"Game Master rolled: {game_master_dice}")
        if 6 in game_master_dice:
            print("Game Master rolled a 6 and won the game! Better luck next time.")
            return False
        print("No 6 rolled this attempt. Moving to the next attempt...\n")
    print("Neither you nor the game master rolled a 6. It's a draw!")
    return False

def chance_challenge():
    challenges = [shell_game, roll_dice_game]
    challenge = random.choice(challenges)
    return challenge()





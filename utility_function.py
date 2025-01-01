def introduction():
    """Display a welcome message for the game and explain the basic rules."""
    print(
        "Welcome to the Fort Boyard game!\n"
        "The aim of the game is to collect three keys to access the treasure room.\n"
        "To collect keys, you must complete challenges.\n"
        "The game is divided into rounds, each round you will have to complete a challenge.\n"
        "The challenges will be either a riddle, a math challenge or a game of chance.\n"
        "You will have to answer correctly to the challenge to earn a key.\n"
        "If you answer incorrectly, the game master will get a key.\n"
        "The game will end when either you or the game master has three keys.\n"
        "The player with three keys first will win the game.\n"
        "Good luck and have fun!\n"
    )

def compose_equipe():
    team = []
    max_players = 3

    while True:
        try:
            num_players = int(input("How many players do you want to include in the team? "))
            if num_players < 1 or num_players > max_players:
                print(f"Error: You can only have between 1 and {max_players} players. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    for i in range(num_players):
        print(f"Enter details for player {i + 1}:")
        name = input("Name: ").strip()
        profession = input("Profession: ").strip()
        is_leader = input("Is this player the team leader? (yes/no): ").strip().lower() == 'yes'
        player = {
            'name': name,
            'profession': profession,
            'is_leader': is_leader,
            'keys_wons': 0
        }
        team.append(player)

    # Ensure there is at least one team leader
    if not any(player['is_leader'] for player in team):
        team[0]['is_leader'] = True

    return team

def challenges_menu():
    """Display the menu for the user to choose the type of challenge and return the choice."""
    print("Choose a challenge type:")
    print("1. Mathematics challenge")
    print("2. Logic challenge")
    print("3. Chance challenge")
    print("4. Père Fouras' riddle")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice < 1 or choice > 4:
                print("Error: Invalid choice. Please enter a number between 1 and 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    return choice

def choose_player(team):
    """Display the list of players and allow the user to select a player to take on the challenge."""
    print("Choose a player to take on the challenge:")
    for i, player in enumerate(team, start=1):
        role = "Leader" if player['is_leader'] else "Member"
        print(f"{i}. {player['name']} ({player['profession']}) - {role}")
    while True:
        try:
            choice = int(input("Enter the player's number: "))
            if choice < 1 or choice > len(team):
                print("Error: Invalid choice. Please enter a number between 1 and", len(team))
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return team[choice - 1]
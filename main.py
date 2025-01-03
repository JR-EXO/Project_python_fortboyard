
from utility_function import *
from logical_challenges import *
from math_challenges import *
from chance_challenges import *
from pere_fouras_challenge import *
from final_challenge import *
def game():
    introduction()
    team = compose_equipe()
    challenge_result = None
    keys_won = 0
    while keys_won < 3:
        challenge_type = challenges_menu()

        player = choose_player(team)
        if challenge_type == 1:
            challenge_result = math_challenge()
        elif challenge_type == 2:
            challenge_result = logical_challenge()
        elif challenge_type == 3:
            challenge_result = chance_challenge()
        elif challenge_type == 4:
            challenge_result = pere_fouras_riddles()

        if challenge_result:
            player['keys_wons'] += 1
            keys_won += 1
            print(f"{player['name']} won a key! Total keys won: {keys_won}")

    treasure_room()  # Assuming a function final_challenge exists
    print("Congratulations! You've completed the game.")

game()
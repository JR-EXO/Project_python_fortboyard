import json
import random

def treasure_room():
    try:
        with open('TRClues.json', 'r') as file:
            tv_game = json.load(file)
    except Exception:
        print("Error loading 'TRClues.json'. Make sure the file exists and is valid.")
        return

    years = list(tv_game.keys())
    if not years:
        print("No data available.")
        return
    year = random.choice(years)
    shows = tv_game[year]
    if not shows:
        print(f"No shows for year {year}.")
        return
    show = random.choice(shows)

    clues = show.get("clues", [])
    code_word = show.get("codeword", "")
    if len(clues) < 3 or not code_word:
        print("Insufficient data in selected show.")
        return

    print("Welcome to the treasure room! Here are your first three clues:")
    for clue in clues[:3]:
        print(clue)
    attempts = 3
    while attempts > 0:
        guess = input("Enter the code word: ").strip()
        if guess.lower() == code_word.lower():
            print("You guessed it! You accessed the treasure room!")
            return
        attempts -= 1
        if attempts > 0:
            print(f"Wrong answer. {attempts} attempts left.")
            if len(clues) > 3:
                print("Additional clue: " + clues[3])
        else:
            print(f"No attempts left. The code word was: {code_word}")


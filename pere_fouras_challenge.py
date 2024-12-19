import json
import random

def load_riddles(file):
    with open(file,"r") as f:
        riddles = json.load(f)
    return riddles

def pere_fouras_riddles():
    riddles = load_riddles("PFRiddles.json")
    if not riddles:
        print("No riddles available. Unable to proceed.")
        return False
    selected_riddle = random.choice(riddles)
    question = selected_riddle.get("question", "No question provided.")
    correct_answer = selected_riddle.get("answer", "").lower()
    attempts = 3
    print("\nHo Ho Ho, I'm the Père Fouras and if you want to get a key, you need to confront me HO HO.")
    print("A riddle will be asked, you will have 3 attempts to achieve the task HO HO.")
    print("Be careful adventurer, if you don't succeed within the three attempts you will lose.")
    print("The riddle is:")
    print(f"Riddle: {question}")
    while attempts > 0:
        player_answer = input("What is your answer adventurer ? : ").strip().lower()
        if player_answer == correct_answer :
            print("Well done Adventurer you just won a key ! Ho HO!")
        else:
            attempts -= 1
            if attempts > 0:
                print(f" HO HO ! Your answer is incorrect! You have {attempts} attempt(s) remaining, Be careful ! HOHO !.")
            else:
                print(f"Ho Ho NO! You have no attempts left adventurer! (looser!!) The correct answer was: {correct_answer}")
                return False
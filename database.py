import json

scores = []

def load_scores():
    global scores
    try:
        with open("scores.json", "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []

def save_score(attempts):
    scores.append(attempts)
    with open("scores.json", "w") as file:
        json.dump(scores, file)

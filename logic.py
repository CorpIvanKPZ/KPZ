import random
import database

secret_number = 0
attempts = 0

def setup_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0

def play_round(guess):
    global attempts
    try:
        guess = int(guess)
        attempts += 1

        if guess < 1 or guess > 100:
            return "Будь ласка, введіть число в межах вказаного діапазону."
        elif guess < secret_number:
            return "Загадане число більше."
        elif guess > secret_number:
            return "Загадане число менше."
        else:
            database.save_score(attempts)
            return f"Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб."
    except ValueError:
        return "Будь ласка, введіть ціле число."

def get_scores_table():
    database.load_scores()
    sorted_scores = sorted(database.scores)
    table = []
    for i, score in enumerate(sorted_scores, start=1):
        table.append([i, score])
    return table

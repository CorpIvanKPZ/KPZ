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
        if not 1 <= guess <= 100:
            return "Будь ласка, введіть число в межах вказаного діапазону."

        attempts += 1
        if guess < secret_number:
            return "Загадане число більше."
        elif guess > secret_number:
            return "Загадане число менше."
        else:
            database.save_score(attempts)
            return f"Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб."
    except ValueError:
        return "Будь ласка, введіть ціле число."

def hint():
    if secret_number % 2 == 0:
        return "Підказка: Загадане число парне."
    else:
        return "Підказка: Загадане число непарне."

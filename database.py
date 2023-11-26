import json
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

scores = []

def load_scores():
    global scores
    try:
        with open("scores.json", "rb") as file:
            encrypted_data = file.read()
            decrypted_data = cipher_suite.decrypt(encrypted_data)
            scores = json.loads(decrypted_data)
    except (FileNotFoundError, json.JSONDecodeError):
        scores = []

def save_score(attempts):
    scores.append(attempts)
    encrypted_data = cipher_suite.encrypt(json.dumps(scores).encode())
    with open("scores.json", "wb") as file:
        file.write(encrypted_data)

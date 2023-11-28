import json
from cryptography.fernet import Fernet

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message

def load_and_decrypt():
    # Load the JSON file
    file_path = "TeamsAndEncryptedMessagesForDistribution.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    # Get the encrypted message associated with the key 'Fulcher'
    encrypted_message = data.get('Fulcher', None)


    key = 'KUtHo1Xqsa2L__6ODtD86Tj-_f5A4nsLvvuUjA2FMmE='
    decrypted_message = decrypt_message(encrypted_message[0], key)

    # Print the decrypted message
    print("Decrypted Message:", decrypted_message)
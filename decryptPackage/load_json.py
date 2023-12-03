import json
from cryptography.fernet import Fernet

def load_fulcher(file_path):
    # Load the JSON file

    with open(file_path, "r") as file:
        data = json.load(file)

    # Get the encrypted message associated with the key 'Fulcher'
    encrypted_message = data.get('Fulcher')
    return encrypted_message

def decrypt_fernet(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message[0])
    print(decrypted_message)
    
#def decrypt_english():
    
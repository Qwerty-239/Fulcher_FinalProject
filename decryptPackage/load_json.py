# load_json.py
# Name: James Speed and John Cannon
# email: speedjp@mail.uc.edu and cannonjp@mail.uc.edu
# Assignment Title: Fulcher Final
# Due Date: 12/7/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that we can use Eclipse to create a PyDev project that executes all the desired functions and code.
# Citations: CHATGPT and Stack Overflow
# Anything else that's relevant: We really do not like SAND!

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
    
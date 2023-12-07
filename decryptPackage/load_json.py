# load_json.py
# Name: James Speed and John Cannon
# email: speedjp@mail.uc.edu and cannonjp@mail.uc.edu
# Assignment Title: Fulcher Final
# Due Date: 12/7/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: modular json reading and splicing function to extract data pertinent to our group
# Citations: CHATGPT and Stack Overflow
# Anything else that's relevant: We really do not like SAND!

import json
from cryptography.fernet import Fernet

def load_fulcher(file_path):
    '''
    author: james speed
    purpose: loads from a json file and extracts data associated with the key 'Fulcher'
    returns: data associated with Fulcher
    '''
    
    # Load the JSON file

    with open(file_path, "r") as file:
        data = json.load(file)

    # Get the encrypted message associated with the key 'Fulcher'
    encrypted_message = data.get('Fulcher')
    return encrypted_message

def decrypt_fernet(encrypted_message, key):
    '''
    author:  James Speed
    purpose: decrypts data using the Fernet library to undo AES encryption
    '''
    
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message[0])
    print(decrypted_message)
    
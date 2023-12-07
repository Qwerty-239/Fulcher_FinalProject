# movie.py
# Name: James Speed and John Cannon
# email: speedjp@mail.uc.edu and cannonjp@mail.uc.edu
# Assignment Title: Fulcher Final
# Due Date: 12/7/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that we can use Eclipse to create a PyDev project that executes all the desired functions and code.
# Citations: CHATGPT and Stack Overflow
# Anything else that's relevant: We really do not like SAND!

from decryptPackage import load_json

def find_movie_name():
    #pulls from load_json.py to obtain encrypted location then decrypt it
    key = 'KUtHo1Xqsa2L__6ODtD86Tj-_f5A4nsLvvuUjA2FMmE='
    encrypted_message = load_json.load_fulcher("TeamsAndEncryptedMessagesForDistribution.json")
    movie_name = load_json.decrypt_fernet(encrypted_message, key)
    return movie_name
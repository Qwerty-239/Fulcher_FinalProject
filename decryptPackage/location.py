# location.py
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
def find_location():
    encrypted_message = load_json.load_fulcher("EncryptedGroupHints Fall 2023 Section 001.json")
    
    with open("english-2.txt", 'r') as file:
        codewords = [line.strip() for line in file.readlines()]
    
    decrypted_message = []
    for x in encrypted_message:
        decrypted_message.append(codewords[int(x)])
    
    return decrypted_message
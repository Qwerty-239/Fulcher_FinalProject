# location.py
# Name: James Speed and John Cannon
# email: speedjp@mail.uc.edu and cannonjp@mail.uc.edu
# Assignment Title: Fulcher Final
# Due Date: 12/7/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: Includes functions relevant to extracting data from json files and decrypting them using Fernet
# Citations: CHATGPT and Stack Overflow
# Anything else that's relevant: We really do not like SAND!

from decryptPackage import load_json
def find_location():
    '''
    author: James Speed
    purpose: takes encrypted data extracted from json file and uses english-2.txt as a cipher to find the location given
    returns: deciphered words as a list because who has time to condense the list into a single string for a one time thing y'know?
    '''
    
    encrypted_message = load_json.load_fulcher("EncryptedGroupHints Fall 2023 Section 001.json")
    
    with open("english-2.txt", 'r') as file:
        codewords = [line.strip() for line in file.readlines()]
    
    decrypted_message = []
    for x in encrypted_message:
        decrypted_message.append(codewords[int(x)])
    
    return decrypted_message
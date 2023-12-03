

from decryptPackage import load_json
def find_location():
    encrypted_message = load_json.load_fulcher("EncryptedGroupHints Fall 2023 Section 001.json")
    
    with open("english-2.txt", 'r') as file:
        codewords = [line.strip() for line in file.readlines()]
    
    decrypted_message = []
    for x in encrypted_message:
        decrypted_message.append(codewords[int(x)])
    
    return decrypted_message
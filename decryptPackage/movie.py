
from decryptPackage import load_json

def find_movie_name():
    #pulls from load_json.py to obtain encrypted location then decrypt it
    key = 'KUtHo1Xqsa2L__6ODtD86Tj-_f5A4nsLvvuUjA2FMmE='
    encrypted_message = load_json.load_fulcher("TeamsAndEncryptedMessagesForDistribution.json")
    movie_name = load_json.decrypt_fernet(encrypted_message, key)
    return movie_name
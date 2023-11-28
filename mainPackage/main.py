

from decryptPackage import load_json
if __name__ == '__main__':
    key = 'KUtHo1Xqsa2L__6ODtD86Tj-_f5A4nsLvvuUjA2FMmE='
    
    encrypted_message = load_json.load_fulcher("TeamsAndEncryptedMessagesForDistribution.json")
    load_json.decrypt_fernet(encrypted_message, key)
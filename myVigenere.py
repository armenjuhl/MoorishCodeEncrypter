def alphabet_position(letter):
    if letter.isupper():       
        upperc_position_letter = ord(letter) - 64      
        return upperc_position_letter

    if letter.islower():
        lowerc_position_letter = ord(letter) - 96      
        return lowerc_position_letter

def rotate_character(char, rot):
    #to passby special characters
    if ord(char) <= 64:
        return chr(ord(char))
    if (ord(char) >= 91) & (ord(char)<= 96):
        return chr(ord(char))
    if (ord(char) >= 123) & (ord(char)<= 127):
        return chr(ord(char))

    if char.isupper():
        alphabetRotate = alphabet_position(char)
        if alphabetRotate > 25:
                alphabetRotate = alphabetRotate % 26
        alphabetRotate = alphabetRotate + 65
        newLetter = chr(alphabetRotate)
        return newLetter
    
    if char.islower():
        alphabetRotate = alphabet_position(char)
        if alphabetRotate > 25:
            alphabetRotate = alphabetRotate % 26
        alphabetRotate = alphabetRotate + 97
        newLetter = chr(alphabetRotate)
        return newLetter

def vigenere(encrypt_text, encryption_key):
    encrypted_text = ""
    i = 0
    encryption_key = encryption_key.lower()
    for word in encrypt_text:
        for char in word:            
            if char == ' ':
                encrypted_text += char                
            encryption_int = ord(encryption_key[i]) -96
            if encryption_key[i] == encryption_key[-1]:
                encrypted_text += rotate_character(char, encryption_int)
                i = 0
            else:
                encrypted_text += rotate_character(char, encryption_int)
                i += 1
    return encrypted_text


def decryptVigenere(decrypt_text, decryption_key):
    encrypted_text = ""
    i = 0
    decryption_key = decryption_key.lower()
    for word in decrypt_text:
        for char in word:            
            if char == ' ':
                encrypted_text += char                
            encryption_int = ord(decryption_key[i]) -96
            encryption_int = 26 - encryption_int % 26
            if decryption_key[i] == decryption_key[-1]:
                encrypted_text += rotate_character(char, encryption_int)
                i = 0
            else:
                encrypted_text += rotate_character(char, encryption_int)
                i += 1
    return encrypted_text

def main():
    if __name__ == "__main__":
        encrypt_text = input("Type a message:\n")
        print(encrypt_text)
        encryption_key = input("Enter the encryption word\n")
        print(encryption_key)
        print(vigenere(encrypt_text, encryption_key))
        decrypt_text = input("Type message to decrypt")
        print(decrypt_text)
        decryption_key = input("Enter the decryption word\n")
        print(decryption_key)
        print(decryptVigenere(decrypt_text, decryption_key))

main()

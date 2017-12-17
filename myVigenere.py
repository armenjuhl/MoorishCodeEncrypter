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


def decryptVigenere(encrypt_text, encryption_key):
    encrypted_text = ""
    i = 0
    decNum = 0
    for word in encrypt_text:
        for char in word:                        
            if char == ' ':
                encrypted_text += char     
            encryption_letter = encryption_key[i]
            encryption_int = alphabet_position(encryption_letter) +1
            decNum = 26 - encryption_int 
            if encryption_key[i] != encryption_key[-1]:
                i = i + 1
            elif encryption_key[i] == encryption_key[-1]:
                i = 0                    
            encrypted_text += rotate_character(char, decNum)
    return encrypted_text

def main():
    if __name__ == "__main__":
        encrypt_text = input("Type a message:\n")
        print(encrypt_text)
        encryption_key = (input("Enter the encryption word\n"))
        print(encryption_key)
        print(vigenere(encrypt_text, encryption_key))

main()

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
        alphabetRotate = alphabet_position(char) + rot
        if alphabetRotate > 25:
                alphabetRotate = alphabetRotate % 26
        alphabetRotate = alphabetRotate + 65
        newLetter = chr(alphabetRotate)
        return newLetter
    
    if char.islower():
        alphabetRotate = alphabet_position(char) + rot
        if alphabetRotate > 25:
            alphabetRotate = alphabetRotate % 26
        alphabetRotate = alphabetRotate + 97
        newLetter = chr(alphabetRotate)
        return newLetter

def vigenere(encrypt_text, encryption_key):
    encrypted_text = ""
    # encryption_key += encryption_key += encryption_key += encryption_key += encryption_key += encryption_key += encryption_key += encryption_key += encryption_key += encryption_key += encryption_key
    for word in encrypt_text:
        for char in word:
            if char == ' ':
                encrypted_text += ' '
            # alpha_num_placeholder = 1
            # int_alpha = int(alpha_num_placeholder)
            # int_alpha = alphabet_position(char)
            text_alpha = alphabet_position(char)
            for letter in encryption_key:
                encryption_alpha = alphabet_position(letter)
             # print(char, "alphabet number is", int_alpha)
                encrypted_text += rotate_character(text_alpha, encryption_alpha)
    return encrypted_text

def main():
    if __name__ == "__main__":
        encrypt_text = input("Type a message:\n")
        print(encrypt_text)
        encryption_key = (input("Enter the encryption key\n"))
        print(encryption_key)
        print(vigenere(encrypt_text, encryption_key))

main()

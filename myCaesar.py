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
        if alphabetRotate > 26:
                alphabetRotate = alphabetRotate % 26
        alphabetRotate = alphabetRotate + 64
        newLetter = chr(alphabetRotate)
        return newLetter
    
    if char.islower():
        alphabetRotate = alphabet_position(char) + rot
        if alphabetRotate > 26:
            alphabetRotate = alphabetRotate % 26
        alphabetRotate = alphabetRotate + 96
        newLetter = chr(alphabetRotate)
        return newLetter

def encrypt(text, rot):
    new_string = ""
    for char in text:
        if char == " ":
            new_string += " "
        new_string = new_string + rotate_character(char, rot)
    return new_string

def decrypt(text, rot):
    new_rot = 26 - rot % 26
    new_string = ""
    for char in text:
        if char == " ":
            new_string += " "
        new_string = new_string + rotate_character(char, new_rot)
    return new_string

def main():
    if __name__ == "__main__":
        text = input("Type a message:\n")
        print(text)
        rot = int(input("Rotate by:\n"))
        print(rot)
        print(encrypt(text, rot))

main()

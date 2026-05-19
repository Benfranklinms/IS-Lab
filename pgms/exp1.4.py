def encrypt(text):

    key = [[3, 3],
           [2, 5]]

    text = text.upper().replace(" ", "")

    if len(text) % 2 != 0:
        text += "X"

    cipher = ""

    for i in range(0, len(text), 2):

        p1 = ord(text[i]) - 65
        p2 = ord(text[i+1]) - 65

        c1 = (3*p1 + 3*p2) % 26
        c2 = (2*p1 + 5*p2) % 26

        cipher += chr(c1 + 65) + chr(c2 + 65)

    return cipher


text = input("Enter plaintext: ")

print("Cipher text:", encrypt(text))
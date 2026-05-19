# Experiment No.: 1.3 - PLAYFAIR CIPHER
# Aim: To implement the Playfair Cipher to encrypt and decrypt a message.

def generate_matrix(key):
    key = key.upper().replace('J', 'I')
    used = []
    for ch in key:
        if ch.isalpha() and ch not in used:
            used.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            used.append(ch)
    matrix = [used[i:i+5] for i in range(0, 25, 5)]
    return matrix

def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                 return i, j

def prepare_text(text):
    text = text.upper().replace('J', 'I')
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2 != 0:
        result += 'X'
    return result

def encrypt(text, matrix):
    text = prepare_text(text)
    cipher = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            cipher += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            cipher += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:
            cipher += matrix[r1][c2] + matrix[r2][c1]
    return cipher

def decrypt(cipher, matrix):
    text = ""
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)
        if r1 == r2:
            text += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            text += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            text += matrix[r1][c2] + matrix[r2][c1]
    return text

key = input("Enter key: ")
plaintext = input("Enter plaintext: ")
matrix = generate_matrix(key)
cipher = encrypt(plaintext, matrix)
decrypted = decrypt(cipher, matrix)
print("\nCipher Text:", cipher.upper())
print("Decrypted Text:", decrypted.lower())

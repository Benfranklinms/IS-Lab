def encrypt(text, key):
    result = ""
    key_index = 0

    for char in text:
        t = ord(char) - 65
        k = ord(key[key_index]) - 65
        result += chr((t + k) % 26 + 65)

        key_index = (key_index + 1) % len(key)

    return result


def decrypt(text, key):
    result = ""
    key_index = 0

    for char in text:
        t = ord(char) - 65
        k = ord(key[key_index]) - 65
        result += chr((t - k) % 26 + 65)

        key_index = (key_index + 1) % len(key)

    return result


text = input("Enter text: ").upper().replace(" ", "")
key = input("Enter key: ").upper()

cipher = encrypt(text, key)
plain = decrypt(cipher, key)

print("Encrypted:", cipher)
print("Decrypted:", plain)

def encrypt(message, key):
    result = ""
    for char in message:
        result = result + chr((ord(char) + key - 65) % 26 + 65)
    return result

def decrypt(message, key):
    result = ""
    for char in message:
        result = result + chr((ord(char) - key - 65) % 26 + 65)
    return result


message = input("enter a message : ").upper()
key = 3

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("encrypted message ", encrypted)
print("decrypted message ", decrypted)

def encrypt(message, key):
    result = ""
    key_index = 0
    for char in message:
        x = ord(char) - 65
        k = ord(key[key_index]) - 65
        result = result + chr((x + k) % 26 + 65)

        key_index = (key_index + 1) % len(k)

        return result


def decrypt(message, key):
    result = ""
    key_index = 0
    for char in message:
        x = ord(char) - 65
        k = ord(key[key_index] - 65)
        result = result + chr((x - k) % 26 + 65)

        key_index = (key_index + 1) % len(key)

        return result


message = input("enter a message : ").upper().replace(" ", "")
key = input("enter a key : ").upper()


def encryption(message, a, b):
    result = ""
    for char in message:
        x = ord(char) - 65
        result = result + chr(((a * x + b) % 26) + 65)
    return result

def decryption(message, a, b):
    result = ""
    a_inv = pow(a, -1, 26)
    for char in message:
        x = ord(char) - 65
        result = result + chr(a_inv * (x - b) % 26 + 65)


text = input("Enter a text : ").upper()

a = int(input("Enter value of a: "))
b = int(input("Enter a value of b: "))


encrypted = encryption(text, a, b)

print("Encryped text is ", encrypted)
print("Decrypted text is ", decryption(encrypted, a, b))

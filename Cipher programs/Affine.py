def encryption(text, a, b):
    result = ""
    for char in text:
        x = ord(char) - 65
        result = result + chr(((a * x + b) % 26) + 65)
    return result

def decryption(text, a, b):
    result = ""
    a_inv = pow(a, -1, 26)
    for char in text:
        x = ord(char) - 65
        result = result + chr(((a_inv * (x - b) % 26) + 65))
    return result


text = input("Enter a text : ").upper()

a = int(input("Enter value of a: "))
b = int(input("Enter a value of b: "))


encrypted = encryption(text, a, b)

print("Encryped text is ", encrypted)
print("Decrypted text is ", decryption(encrypted, a, b))

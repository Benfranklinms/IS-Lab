def encryption(text):
    result = ""
    for char in text:
        result = result + chr((ord(char) + key - 65) % 26 + 65)
    return result

def decryption(text):
    result = ""
    for char in text:
        result = result + chr((ord(char) - key - 65) % 26 + 65)
    return result


key = 3
text = input("Enter a text to encrypt : ").upper()
result1 = encryption(text)
result2 = decryption(result1)

print("Encypted text is ", result1)
print("Decrypted text is ", result2)

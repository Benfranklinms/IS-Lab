key = [[3, 3],
       [4, 3]]

text = input("Enter a text : ").upper().replace(" ", "")

if len(text) % 2 != 0:
    text = text + "X"

cipher = ""

for i in range(0, len(text), 2):
    p1 = ord(text[i]) - 65
    p2 = ord(text[i + 1]) - 65

    c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
    c2 = (key[0][1] * p1 + key[1][1] * p2) % 26

    cipher = cipher + chr(c1 + 65) + chr(c2 + 65)

print("cipher text is : ", cipher)

key = input("Enter key: ").upper()
text = input("Enter plaintext: ").upper()

m = ""

for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch not in m:
        m += ch

if len(text) % 2 != 0:
    text += "X"

cipher = ""

for i in range(0, len(text), 2):

    a = m.index(text[i])
    b = m.index(text[i+1])

    r1, c1 = a//5, a%5
    r2, c2 = b//5, b%5

    if r1 == r2:
        cipher += m[r1*5 + (c1+1)%5]
        cipher += m[r2*5 + (c2+1)%5]

    elif c1 == c2:
        cipher += m[((r1+1)%5)*5 + c1]
        cipher += m[((r2+1)%5)*5 + c2]

    else:
        cipher += m[r1*5 + c2]
        cipher += m[r2*5 + c1]

print("Cipher:", cipher)
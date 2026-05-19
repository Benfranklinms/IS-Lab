# Experiment No.: 1.4 - HILL CIPHER (with Encryption and Decryption)
# Aim: To design and implement the Hill Cipher algorithm for encrypting
# and decrypting text using a key matrix with modular arithmetic.

def encrypt(pt, key):
    pt = pt.upper().replace(" ", "")
    if len(pt) % 2 != 0:
        pt += 'X'

    ct = ""
    for i in range(0, len(pt), 2):
        p1 = ord(pt[i]) - 65
        p2 = ord(pt[i+1]) - 65

        c1 = (key[0][0]*p1 + key[0][1]*p2) % 26
        c2 = (key[1][0]*p1 + key[1][1]*p2) % 26

        ct += chr(c1 + 65) + chr(c2 + 65)
    return ct

def decrypt(ct, key):
    det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26

    det_inv = -1
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break

    inv_key = [
        [(key[1][1] * det_inv) % 26, (-key[0][1] * det_inv) % 26],
        [(-key[1][0] * det_inv) % 26, (key[0][0] * det_inv) % 26]
    ]

    pt = ""
    for i in range(0, len(ct), 2):
        c1 = ord(ct[i]) - 65
        c2 = ord(ct[i+1]) - 65

        p1 = (inv_key[0][0]*c1 + inv_key[0][1]*c2) % 26
        p2 = (inv_key[1][0]*c1 + inv_key[1][1]*c2) % 26

        pt += chr(p1 + 65) + chr(p2 + 65)
    return pt

key = [[3, 3], [2, 5]]
plain_text = input("Input the plain_text : ")
cipher_text = encrypt(plain_text, key)
decrypted_text = decrypt(cipher_text, key)
print("Encrypted:", cipher_text)
print("Decrypted:", decrypted_text)

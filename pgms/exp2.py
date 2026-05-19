import math

p = int(input("Enter a number : "))
q = int(input("Enter a number : "))

n = p * q

phi = (q - 1) * (p - 1)

for i in range(2, phi):
    if math.gcd(i, phi) == 1:
        e = i
        break

d = pow(e,-1, phi)

print("Public key : ", (e, n))
print("Private key : ", (d, n))

m = int(input("Enter a message : "))

cipher = pow(m, e, n)

print("Cipher text is ", cipher)

msg = pow(cipher, d, n)

print("Decrypted message is ", msg)

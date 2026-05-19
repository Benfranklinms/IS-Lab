# Experiment No.: 4 - RSA DIGITAL SIGNATURE
# Aim: To implement RSA Digital Signature, by generating keys, hashing a message,
# signing it using the private key, and verifying it using the public key.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def simple_hash(message):
    hash_value = 0
    for ch in message:
        hash_value = (hash_value * 31 + ord(ch))
    return hash_value

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
n = p * q
phi = (p - 1) * (q - 1)
e = 3
while gcd(e, phi) != 1:
    e += 2
d = mod_inverse(e, phi)
message = input("Enter message: ")
hash_val = simple_hash(message)
print("Hash value:", hash_val)
signature = pow(hash_val, d, n)
print("Signature:", signature)
verified_hash = pow(signature, e, n)
new_hash = simple_hash(message)
print("Verified Hash:", verified_hash)
if verified_hash == new_hash % n:
    print("Signature is valid")
else:
    print("Signature is invalid")

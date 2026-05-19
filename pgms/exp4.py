import math

def simple_hash(message):
    value = 0

    for ch in message:
        value = value + ord(ch)

    return value


p = int(input("enter a number : "))
q = int(input("enter a number : "))

n = p * q

phi = (q - 1) * (p - 1)

for i in range(2, phi):
    if math.gcd(i, phi) == 1:
        e = i
        break

d = pow(e, -1, phi)

print("public keys ", (e, n))
print("private keys ", (d, n))

message = input("enter a message : ")

hash_value = simple_hash(message)

signature = pow(hash_value, d, n)
print("signature ", signature)

verify = pow(signature, e, n)
print("verified hash", verify)

if verify == hash_value % n:
    print("hash is verified")
else:
    print("hash is not verified")

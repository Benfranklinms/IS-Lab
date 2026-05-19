# Experiment No.: 2 - RSA
# Aim: To implement the RSA asymmetric cryptographic algorithm to generate
# a public and private key pair and to perform encryption and decryption.

from sympy import mod_inverse, gcd

def generate_keys():
    p = int(input("Enter p value: "))
    q = int(input("Enter q value: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    possible_e_vals = [e for e in range(2, phi) if gcd(e, phi) == 1]

    print("\nPossible values of e:")
    print(possible_e_vals)

    e = int(input("\nSelect an e value: "))

    d = mod_inverse(e, phi)

    print(f"\nPublic Key (e={e}, n={n})")
    print(f"Private Key (d={d}, n={n})")

    return (e, n), (d, n)

def encrypt(M, public_key):
    e, n = public_key
    C = pow(M, e, n)
    return C

def decrypt(C, private_key):
    d, n = private_key
    M = pow(C, d, n)
    return M

public_key, private_key = generate_keys()
M_input = int(input("\nEnter numeric value to encrypt: "))
C = encrypt(M_input, public_key)
print(f"Encrypted message: {C}")
C_input = int(input("\nEnter numeric value to decrypt: "))
M = decrypt(C_input, private_key)
print(f"Decrypted message: {M}")

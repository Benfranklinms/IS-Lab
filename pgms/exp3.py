import hashlib

s1 = input("Enter a string : ")
h1 = hashlib.sha256(s1.encode()).hexdigest()

print("Hash 1 : ", h1)

s2 = input("Enter a string : ")
h2 = hashlib.sha256(s2.encode()).hexdigest()

print("Hash 2 : ", h2)

h1_bytes = bytes.fromhex(h1)
h2_bytes = bytes.fromhex(h2)

h1_int = int.from_bytes(h1_bytes, byteorder = "big")
h2_int = int.from_bytes(h2_bytes, byteorder = "big")

xor_result = h1_int ^ h2_int

bit_difference = bin(xor_result).count('1')

print("bit difference : ", bit_difference)

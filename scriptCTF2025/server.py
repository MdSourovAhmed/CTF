# import os
# from pwn import xor
# print("With the Secure Server, sharing secrets is safer than ever!")
# enc = bytes.fromhex(input("Enter the secret, XORed by your key (in hex): ").strip())
# key = os.urandom(32)
# enc2 = xor(enc,key).hex()
# print(f"Double encrypted secret (in hex): {enc2}")
# dec = bytes.fromhex(input("XOR the above with your key again (in hex): ").strip())
# secret = xor(dec,key)
# print("Secret received!")








def custom_xor(a, b):
    if len(a) != len(b):
        raise ValueError("Byte strings must have equal length")
    return bytes(x ^ y for x, y in zip(a, b))

# Provided hex inputs
enc = bytes.fromhex("151e71ce4addf692d5bac83bb87911a20c39b71da3fa5e7ff05a2b2b0a83ba03")
enc2 = bytes.fromhex("e1930164280e44386b389f7e3bc02b707188ea70d9617e3ced989f15d8a10d70")
dec = bytes.fromhex("87ee02c312a7f1fef8f92f75f1e60ba122df321925e8132068b0871ff303960e")

# Compute server_key
server_key = custom_xor(enc, enc2)

# Compute secret
secret_bytes = custom_xor(dec, server_key)

# Decode to text
secret = secret_bytes.decode('ascii')
print(secret)

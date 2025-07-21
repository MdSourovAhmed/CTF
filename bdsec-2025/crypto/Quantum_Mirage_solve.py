import base64
import hashlib
from Crypto.Util.number import *

# Constants from quantum.py
X = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476,
     0xC3D2E1F0, 0x76543210, 0xFEDCBA98, 0x89ABCDEF]

def G(a, b):
    d = a
    for i in range(b):
        if i % 4 == 0:
            d = hashlib.sha256(d).digest()
        elif i % 4 == 1:
            d = hashlib.blake2b(d, digest_size=32).digest()
        elif i % 4 == 2:
            d = hashlib.md5(d).digest() * 2
        else:
            d = hashlib.sha1(d).digest() + d[:12]
    return d

def reverse_H(q, k):
    m = bytearray()
    for i, s in enumerate(q):
        # Reverse XOR with X
        s = s ^ (X[i % len(X)] & 0xFF)
        # Reverse rotation: Find u such that ((u << 3) | (u >> 5)) & 0xFF = s
        for u in range(256):
            if ((u << 3) | (u >> 5)) & 0xFF == s:
                break
        # Reverse XOR with key
        t = u ^ k[i % len(k)]
        m.append(t & 0xFF)
    return bytes(m)

# Intercepted message
message = "FL6gWSgGl71j8RANN2yzz9XckwawQ8MXqE7IAOVygOclZiHgi161L7s="

# Decode base64
decoded_message = base64.b64decode(message)

# Compute key
b = b"simple_seed_123"
key = G(b, 5)

# Reverse H function to get original message
original_msg = reverse_H(decoded_message, key)

# Print result
print("Decoded message:", original_msg.decode())

def decode_char(encoded: str, base: int) -> str:
    """Decode a digit string in given base back to a character"""
    value = int(encoded, base)
    return chr(value)

with open("based.txt", 'rb') as f:
    text = f.read().strip()

# Reverse the process: bases 2 → 10
for base in range(2, 11):
    parts = text.split()
    text = "".join(decode_char(part, base) for part in parts)

print("Recovered flag:", text)

import base64

# Input string
input_str = '3d3d516343746d4d6d6c315669563362'

# Convert from hexadecimal to binary
binary_data = bytes.fromhex(input_str)

# Reverse the binary data
reversed_data = binary_data[::-1]

# Decode the reversed data from Base64
decoded_data = base64.b64decode(reversed_data)

# Print the result
print(decoded_data.decode('utf-8'))

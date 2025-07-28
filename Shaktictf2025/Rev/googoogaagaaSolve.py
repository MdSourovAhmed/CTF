key = "IWANTMOMOS"
encrypted = [':', '?', ' ', '%', ' ', '$', ',', '9', ')', '(', '+', 'c', '#', '7', '\x06', '~', '9', '\x12', '~', ' ', '\x16', '4', '4', ':', 'g', '0']

result = ''
for i in range(len(encrypted)):
    result += chr(ord(encrypted[i]) ^ ord(key[i % len(key)]))

print(result)

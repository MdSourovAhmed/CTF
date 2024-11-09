msg = "L|k¤y+*^*zo¤*¤kvsno|*k¤om*vo*zk}}*cyvksr"

for x in range(256):
    print(f"{x}) ")
    print( ''.join([chr((ord(y) + x) % 256) for y in msg]))

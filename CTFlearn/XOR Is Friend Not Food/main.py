code = "\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e"
unciphered = "ctflearn{"
BLOCK_XOR_KEY_SIZE = 5

block_xor_key = []

for i in range(BLOCK_XOR_KEY_SIZE):
    block_xor_key += [ord(code[i]) ^ ord(unciphered[i])]

for i in range(len(code)):
    xor_key = block_xor_key[i % len(block_xor_key)]
    char = chr(ord(code[i]) ^ xor_key)
    print(char, end='')

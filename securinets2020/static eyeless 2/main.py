import random

char_arr = [0xd1, 0x1e, 0xdb, 0xfb, 0x74, 0xcb, 0x15, 0xdd, 0xfa, 0x75, 0xd9, 0x4b, 0xda, 0xe8, 0x73, 0xd1, 0x4f, 0xcc,
            0xe7, 0x36, 0xcc, 0x4e, 0xe7, 0xfc, 0x36, 0xc1, 0x10, 0x8d, 0xaf, 0x7b, 0xa8]
block_xor_key = [0xa2, 0x7b, 0xb8, 0x8e, 0x06]
iter = 0
for char in char_arr:
    xor_key = block_xor_key[iter % len(block_xor_key)]
    print(chr((char) ^ (xor_key)), end='')
    iter += 1

print()

key = [
    0xf6, 0x9b, 0x05, 0xfe,
    0x36, 0xa3, 0x3e, 0x93,
    0xc8, 0x2c, 0xb2, 0x6e,
    0x33, 0x7c, 0x93, 0x2a,
    0xc4, 0x6e, 0xa4, 0x0f,
    0x8c, 0xd8, 0x7d, 0xdf,
    0xae, 0xc6, 0x7c, 0xd7,
    0xef, 0xa5, 0x71, 0x48,
    0xc8, 0x49, 0x3a, 0xb2,
    0x78, 0xf5, 0xcc, 0xbe,
    0x9a, 0x47, 0xd2, 0x87,
    0x10, 0xfd]

# random seq given 's' as a seed
seq = [
    0x9f, 0xc4, 0x77, 0xcd,
    0x02, 0xcf, 0x52, 0xea,
    0x97, 0x4e, 0x81, 0x02,
    0x02, 0x4f, 0xe5, 0x19,
    0x9b, 0x5f, 0xca, 0x50,
    0xf9, 0xaa, 0x22, 0xb9,
    0xdb, 0xb2, 0x09, 0xa5,
    0xdc, 0xfa, 0x03, 0x7b,
    0xbe, 0x7a, 0x48, 0xc1,
    0x49, 0x9b, 0xab, 0xe1,
    0xe9, 0x2c, 0xe3, 0xeb,
    0x7c, 0xc8, 0x05, 0x17,
    0x27, 0xcf]

random.seed(ord('s'))

for char, xor in zip(key, seq):
    print(chr(char ^ random.randint(0x0, 0xff)), end='')


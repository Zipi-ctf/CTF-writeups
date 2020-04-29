xored_flag = "IdontKnowWhatsGoingOn"
block_xor_key = [0x00000008, 0x00000006, 0x0000002c, 0x0000003a, 0x00000032, 0x00000030, 0x0000001c, 0x0000005c,
                 0x00000001, 0x00000032, 0x0000001a, 0x00000012, 0x00000045, 0x0000001d, 0x00000020, 0x00000030,
                 0x0000000d, 0x0000001b, 0x00000003, 0x0000007c, 0x00000013]

for xored_char, xor_key in zip(xored_flag, block_xor_key):
    char = chr(ord(xored_char) ^ xor_key)
    print(char, end='')

xored_flag = [0x63, 0x60, 0x69, 0x7e, 0x6c, 0x51, 0x49, 0x42, 0x19, 0x49, 0x41, 0x75, 0x1b, 0x44, 0x1b, 0x5e, 0x75,
              0x48, 0x1e, 0x4c, 0x1a, 0x58, 0x19, 0x75, 0x47, 0x1e, 0x1b, 0x44, 0x57]

key = 0x2a

for xored_char in xored_flag:
    char = chr(xored_char ^ key)
    print(char, end='')

from string import printable

flag = "q{vpln'bH_varHuebcrqxetrHOXEj"
print_string = ""
for xor_key in range(256):
    for xored_char in flag:
        char = chr(ord(xored_char) ^ xor_key)
        if char not in printable:
            print_string = ""
            break
        print_string += char
    if len(print_string) != 0:
        print("flag: {} | xor_key: {}".format(print_string, xor_key))
        print_string = ""
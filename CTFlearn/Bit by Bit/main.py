import base64

b64_test_strings = [("YWxiYXRyb3Nzfl4mfH58Xnw=", -1), ("Y3RmbGVhcm5ePj5+Pj5+Pj58", 1331000),
                    ("c3BhZ2hldHRpJj4+fn58fl4m", 10393),
                    ("aWJldHlvdWp1c3R0cmllZHRoaXNiZWNhdXNleW91d2FudGVkdG9rbm93d2hhdHRoZW1lc3NhZ2V3YXNeXj4+Xl4mfD4+fCZ8Pj4+PiZePj5+Pj5ePj5ePj4+Pj4+fj4+Pj58fiZ8fCZ8fH4+Pn4+Pn5efH5efl58fCZ8Pj5+Pj5+Pj58JiY=", 74785)]

b64_string_flag = "YmluYXJ5cmVmaW5lcnl8JiY+PnxeXl4mJnx8fg=="

def extract_stringbytes_and_operators(byte_array):
    extracted_operators = []
    i = 0
    string_end = 0
    while i < len(byte_array):
        if byte_array[i] in b'|~><&^':
            extracted_operators.append(byte_array[i])
            if byte_array[i] in b'><':
                i += 1
        else:
            string_end = i
        i += 1
    return byte_array[:string_end+1], extracted_operators


def calculate_checksum(input_string):
    operator_dictionary = {
        ord('|'): lambda lhv, rhv : lhv | rhv,
        ord('~'): lambda lhv, rhv : ~lhv,
        ord('>'): lambda lhv, rhv: lhv >> rhv,
        ord('<'): lambda lhv, rhv: lhv << rhv,
        ord('&'): lambda lhv, rhv: lhv & rhv,
        ord('^'): lambda lhv, rhv: lhv ^ rhv
    }

    extracted_string_bytes, extracted_operators = extract_stringbytes_and_operators(base64.b64decode(input_string))
    resulting_checksum = int(extracted_string_bytes[0]) ** 3
    for j in range(len(extracted_string_bytes) - 1):
        for i in range(j, len(extracted_string_bytes) - 1, 1):
            resulting_checksum = operator_dictionary[extracted_operators[i]](resulting_checksum, int(extracted_string_bytes[i+1]) ** 3)
    return resulting_checksum


for string, expected_value in b64_test_strings:
    print("{} : expected {} got {}".format(base64.b64decode(string), expected_value, calculate_checksum(string)))

print("===CTF solution===")
print("{} : {} : {}".format(b64_string_flag, base64.b64decode(b64_string_flag), calculate_checksum(b64_string_flag)))

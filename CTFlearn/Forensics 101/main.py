from string import printable

file = open("95f6edfb66ef42d774a5a34581f19052.jpg", mode='rb')
filter = 9
print_string = ''
for byte in file.read():
    char = chr(int(byte))
    if char in printable:
        print_string += char
    else:
        if len(print_string) >= filter:
            print(print_string)
        print_string = ''

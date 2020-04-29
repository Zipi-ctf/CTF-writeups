file = open("data.dat")

lines = file.readlines()
number_of_lines = 0
for line in lines:
    if line.count('0') % 3 == 0 or line.count('1') % 2 == 0:
        number_of_lines += 1

print(number_of_lines)

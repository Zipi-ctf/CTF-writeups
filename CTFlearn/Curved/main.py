from string import printable
from PIL import Image
import numpy as np

image = Image.open("stego.png")
image_array = np.asarray(image)
data_array = []
for row in image_array:
    for pixel in row:
        data_array += [int(pixel[0]) - int(pixel[2])]
char_array = []
temp_char = 0
for bit_number in range(len(data_array)):
    temp_char *= 2
    temp_char += abs(data_array[bit_number])
    if bit_number % 8 == 7:
        char_array += [temp_char]
        temp_char = 0

for hex in char_array:
    print(chr(hex), end='')

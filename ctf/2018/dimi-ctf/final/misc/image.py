from PIL import Image
import re
import struct

f = open('imageResult', 'wb')

im = Image.open('prob.png')
for x in range(im.width):
    for y in range(im.height):
        pixel = im.getpixel((x, y))
        f.write(struct.pack('B', pixel[0]))
        f.write(struct.pack('B', pixel[1]))
        f.write(struct.pack('B', pixel[2]))

f.close()
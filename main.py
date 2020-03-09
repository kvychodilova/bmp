"""with open('test.bmp', 'rb') as f:
    data = bytearray(f.read())
print(data)
"""
import random, sys
from PIL import Image
import numpy as np
import math
import struct
from pip._vendor.urllib3.connectionpool import xrange

# bmp = open('test.bmp', 'rb')

bmp = Image.open('new.bmp').convert('RGB')
pixels = list(bmp.getdata())
width, height = bmp.size
#print(pixels)
print("nic")

zkouska = np.asarray(bmp).copy()
"""
def rotate_image(img):
    bmp = Image.open('new.bmp').convert('RGB')
    width, height = bmp.size

    w = width-1
    y = 0
    while y < w:
        x = y
        wy = w - y
        while x < wy:
            wx = w - x
            p1 = img[y][x]
            img  [y][x]  = img [wx][y]
            img [wx][y]  = img [wy][wx]
            img [wy][wx] = img  [x][wy]
            img  [x][wy] = p1
            x += 1
        y += 1
    return img
"""
from PIL import Image, ImageDraw

# Load image:
input_image = Image.open("test2.bmp").convert('RGB')
input_pixels = input_image.load()

# Create output image
output_image = Image.new("RGB", input_image.size,'white')
#pixels = output_image.load()
draw = ImageDraw.Draw(output_image)

angle = 1.5708  # angle in radian
center_x = input_image.width / 2
center_y = input_image.height / 2

# Copy pixels
for x in range(output_image.width):
    for y in range(output_image.height):
        xp = input_image.width - x - 1
        draw.point((x, y), input_pixels[xp, y])



output_image.show()
#output_image.save("output.bmp")


"""
def rotateMatrix(mat):

    if not len(mat):
        return


        #top : starting row index
        #bottom : ending row index
        #left : starting column index
        #right : ending column index


    top = 0
    bottom = len(mat)-1

    left = 0
    right = len(mat[0])-1

    while left < right and top < bottom:

        # Store the first element of next row,
        # this element will replace first element of
        # current row
        prev = mat[top+1][left]

        # Move elements of top row one step right
        for i in range(left, right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr

        top += 1

        # Move elements of rightmost column one step downwards
        for i in range(top, bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr

        right -= 1

        # Move elements of bottom row one step left
        for i in range(right, left-1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr

        bottom -= 1

        # Move elements of leftmost column one step upwards
        for i in range(bottom, top-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr

        left += 1

    return mat

# Utility Function
def printMatrix(mat):
    for row in mat:
        print(row)

zkouska = np.asarray(bmp)
zkouska=zkouska.copy()
matrix = rotateMatrix(zkouska)


# Print rotated matrix
#copy.show()

nove=Image.fromarray(matrix,'RGB')
nove.show()
"""


"""
#01
for x in range(200):
  for y in range(200):
    p = sourceImage.getpixel(x,y) # copy a pixel
    targetImage.getpixel(y,x,p)   # put it in the new image, rotated 90 deg

#02
zkouska = np.asarray(bmp)
print(zkouska)
dal = zkouska.tolist()
print(bmp.size)
print(len(dal))
"""
"""
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel


def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

def convert_grayscale(image):
  # Get size
  width, height = image.size

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()

  # Transform to grayscale
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = get_pixel(image, i, j)

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Transform to grayscale
      gray = (red * 0.333) + (green * 0.333) + (blue * 0.333)

      # Set Pixel in new image
      pixels[i, j] = (int(gray), int(gray), int(gray))

  # Return new image
  return new

def invert(image):
  # Get size
  width, height = image.size

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()

  # Transform to grayscale
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = get_pixel(image, i, j)

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Transform to grayscale
      gray = (255-red) + (255-green) + (255-blue)

      # Set Pixel in new image
      pixels[i, j] = (int(gray), int(gray), int(gray))

  # Return new image
  return new
"""

#a=convert_grayscale(bmp)
#a=invert(bmp)
#a.show()
#ulození 4bit pochybné
#bmp.save('novy.bmp',bit=4)
"""
import imageio
img = imageio.imread('test.bmp')
print(img)
print(img.shape)
print(img.reshape((width,height)))


"""
#print(width)
"""Funguje - otáčení
transposed  = bmp.transpose(Image.ROTATE_90)
transposed.show()
"""




#new_img = bmp.resize( (256, 256) )
#new_img.save('new.bmp','bmp')
"""
bmp = open('test3.bmp', 'rb')
print('Type:', bmp.read(2).decode())
print('Size: %s' % struct.unpack('I', bmp.read(4)))
print('Reserved 1: %s' % struct.unpack('H', bmp.read(2)))
print('Reserved 2: %s' % struct.unpack('H', bmp.read(2)))
print('Offset: %s' % struct.unpack('I', bmp.read(4)))
print('DIB Header Size: %s' % struct.unpack('I', bmp.read(4)))
print('Width: %s' % struct.unpack('I', bmp.read(4)))
print('Height: %s' % struct.unpack('I', bmp.read(4)))
print('Colour Planes: %s' % struct.unpack('H', bmp.read(2)))
print('Bits per Pixel: %s' % struct.unpack('H', bmp.read(2)))
print('Compression Method: %s' % struct.unpack('I', bmp.read(4)))
print('Raw Image Size: %s' % struct.unpack('I', bmp.read(4)))
print('Horizontal Resolution: %s' % struct.unpack('I', bmp.read(4)))
print('Vertical Resolution: %s' % struct.unpack('I', bmp.read(4)))
print('Number of Colours: %s' % struct.unpack('I', bmp.read(4)))
print('Important Colours: %s' % struct.unpack('I', bmp.read(4)))

print(" ")
"""
"""
bmp2 = open('novy.bmp', 'rb')
print('Type:', bmp2.read(2).decode())
print('Size: %s' % struct.unpack('I', bmp2.read(4)))
print('Reserved 1: %s' % struct.unpack('H', bmp2.read(2)))
print('Reserved 2: %s' % struct.unpack('H', bmp2.read(2)))
print('Offset: %s' % struct.unpack('I', bmp2.read(4)))
print('DIB Header Size: %s' % struct.unpack('I', bmp2.read(4)))
print('Width: %s' % struct.unpack('I', bmp2.read(4)))
print('Height: %s' % struct.unpack('I', bmp2.read(4)))
print('Colour Planes: %s' % struct.unpack('H', bmp2.read(2)))
print('Bits per Pixel: %s' % struct.unpack('H', bmp2.read(2)))
print('Compression Method: %s' % struct.unpack('I', bmp2.read(4)))
print('Raw Image Size: %s' % struct.unpack('I', bmp2.read(4)))
print('Horizontal Resolution: %s' % struct.unpack('I', bmp2.read(4)))
print('Vertical Resolution: %s' % struct.unpack('I', bmp2.read(4)))
print('Number of Colours: %s' % struct.unpack('I', bmp2.read(4)))
print('Important Colours: %s' % struct.unpack('I', bmp2.read(4)))
"""

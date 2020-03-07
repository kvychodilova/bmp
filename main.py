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

bmp = Image.open('test3.bmp').convert('RGB')
pixels = list(bmp.getdata())
width, height = bmp.size
print(pixels)
print("nic")

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

#a=convert_grayscale(bmp)
a=invert(bmp)
a.show()
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

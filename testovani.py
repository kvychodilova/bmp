import sys
from tkinter.tix import Form


from PIL import Image
import struct
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,\
    QPushButton, QVBoxLayout, QBoxLayout, QHBoxLayout, QGridLayout, QFileDialog


import sys


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,\
    QPushButton, QVBoxLayout, QBoxLayout, QHBoxLayout, QGridLayout, QFileDialog

from PIL import Image
import struct


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._open_button = QPushButton("Otevrit", self)
        self._grayscale_button = QPushButton("Odstiny sedi", self)

        self._image_label = QLabel()
        self._info_label = QLabel()

        #self._image = QPixmap('new.bmp')
        #self._label.setPixmap(self._image)
        #self.resize(self._image.width(),self._image.height())


        grid = QGridLayout()
        grid.addWidget(self._open_button,0,0)
        grid.addWidget(self._grayscale_button,0,1)

        grid.addWidget(self._image_label, 1,0)
        #layout_data.addStretch()
        grid.addWidget(self._info_label,2,0)



        self.setLayout(grid)

        self._open_button.clicked.connect(self.select)
        self._grayscale_button.clicked.connect(self.grayscale_filter)




    def grayscale_filter(self):
        def get_pixel(image, i, j):
            # Inside image bounds?
            width, height = image.size
            if i > width or j > height:
              return None

            # Get Pixel
            pixel = image.getpixel((i, j))
            return pixel
        print(soubor)
         # Get Image and size
        bmp = Image.open(soubor).convert('RGB')             #!!!!!!!!!!!!!
        width, height = bmp.size

        # Create new Image and a Pixel Map
        new = Image.new("RGB", (width, height), "white")
        pixels = new.load()
        #print('nnjnj'+pixels)


        # Transform to grayscale
        for i in range(width):
            for j in range(height):
              # Get Pixel
              pixel = get_pixel(bmp, i, j)

              # Get R, G, B values (This are int from 0 to 255)
              red =   pixel[0]
              green = pixel[1]
              blue =  pixel[2]

              # Transform to grayscale
              gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

              # Set Pixel in new image
              pixels[i, j] = (int(gray), int(gray), int(gray))

        # Return new image
        new.show()
        return


    def select(self, pomocna=None):
        fname = QFileDialog.getOpenFileName(None, 'Nahrat BMP',
        'c:\\',"Image files (*.bmp)")
        print(fname)
        print(fname[0])

        self._image = QPixmap(fname[0])
        self._image_label.setPixmap(self._image)

        bmp = open(fname[0], 'rb')
        self._info_label.setText(str(
                'Typ: ' + bmp.read(2).decode()+ '\n'
                'Velikost: %s' % struct.unpack('I', bmp.read(4)))+ '\n'
                'Reserved 1: %s' % struct.unpack('H', bmp.read(2))+ '\n'
                'Reserved 2: %s' % struct.unpack('H', bmp.read(2)) + '\n'
                'Offset - obrazová data: %s' % struct.unpack('I', bmp.read(4))    + '\n'
                'Velikost hlavičky: %s' % struct.unpack('I', bmp.read(4))   + '\n'
                'Šířka(pixel): %s' % struct.unpack('I', bmp.read(4))+ '\n'
                'Výška(pixel): %s' % struct.unpack('I', bmp.read(4))  + '\n'
                'Počet bitových rovin: %s' % struct.unpack('H', bmp.read(2))+ '\n'
                'Bits per Pixel(počet barev): %s' % struct.unpack('H', bmp.read(2))     + '\n'
                'Komprese : %s' % struct.unpack('I', bmp.read(4))+ '\n'
                'Velikost obrazových dat: %s' % struct.unpack('I', bmp.read(4))+ '\n'
                'Horizontální rozlišení: %s' % struct.unpack('I', bmp.read(4))+ '\n'
                'Vertikální rozlišení: %s' % struct.unpack('I', bmp.read(4))+ '\n'
                'Počet použitých barev: %s' % struct.unpack('I', bmp.read(4))+ '\n'
                'Důležité barvy: %s' % struct.unpack('I', bmp.read(4))+ '\n'
                 )
        global soubor
        soubor = fname[0]
        return



app = QApplication(sys.argv)
w = MainWindow()
w.setWindowTitle("Bitmap")
#w.setGeometry(900,500,500,200)
w.show()
sys.exit(app.exec())


"""
from PIL import Image

# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'bmp')


# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image


# Get the pixel from the given image
def get_pixel(image, i, j):
  # Inside image bounds?
  width, height = image.size
  if i > width or j > height:
    return None

  # Get Pixel
  pixel = image.getpixel((i, j))
  return pixel


# Main
original = open_image('test3.bmp').convert('RGB')
print(get_pixel(original, 1,1))
width, height = original.size
new = create_image(width, height)
pixels = new.load()
nahrazka = original
for i in range(width):
    for j in range(height):

        # Get Pixel
      pixel = nahrazka.getpixel((i, j))

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Transform to grayscale
      gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

      # Set Pixel in new image
      pixels[i, j] = (int(gray), int(gray), int(gray))


"""

"""
class filedialogdemo(QWidget):
    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)

        layout = QVBoxLayout()
        self.btn = QPushButton("QFileDialog static method demo")
        self.btn.clicked.connect(self.getfile)

        layout.addWidget(self.btn)
        self.le = QLabel("Hello")

        layout.addWidget(self.le)
        self.btn1 = QPushButton("QFileDialog object")
        self.btn1.clicked.connect(self.getfiles)
        layout.addWidget(self.btn1)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("File Dialog demo")

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Image files (*.jpg *.gif)")
        self.le.setPixmap(QPixmap(fname))

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        filenames = QStringList()

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.contents.setText(data)


def main():
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
"""
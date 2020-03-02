import sys


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

        layout = QHBoxLayout()
        layout.addWidget(self._open_button)
        layout.addWidget(self._grayscale_button)

        grid.addLayout(layout,1,1)

        layout_data = QGridLayout()
        layout_data.addWidget(self._image_label, 1,1)
        #layout_data.addStretch()
        layout_info = QGridLayout()
        layout_info.addWidget(self._info_label,1,2)


        grid.addLayout(layout_data,3,1)
        grid.addLayout(layout_info,2,2)
        self.setLayout(layout_info)
        self.setLayout(layout)
        self.setLayout(layout_data)
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
w.setGeometry(10,10,300,200)
w.show()
sys.exit(app.exec())

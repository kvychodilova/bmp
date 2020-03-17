import sys


from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,\
    QPushButton, QVBoxLayout, QBoxLayout, QHBoxLayout, QGridLayout, QFileDialog, QFrame, QMessageBox

from PIL import Image, ImageDraw
import struct


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        #Tlacitka - Nacteni
        self._open_button = QPushButton("Otevrit", self)
        self._open_button.setStyleSheet("background-color:#16f6c3;"
                                        "border-style: outset;border-width:"
                                        " 2px;border-radius: 10px;border-color: beige;"
                                        "font: bold 14px;min-width: 10em;padding: 6px;")
        #Tlacitka - Uprava barev
        self._text_barvy = QLabel()
        self._text_barvy.setText('Upravit barvy')
        self._text_barvy.setAlignment(Qt.AlignCenter)
        self._grayscale_button = QPushButton("Odstiny sedi", self)
        self._grayscale_button.setStyleSheet("background-color:#b3b3b3;"
                                             "border-style: outset;border-width:"
                                        " 2px;border-radius: 10px;border-color: beige;"
                                        "font: bold 14px;min-width: 10em;padding: 6px;")

        self._invers_button = QPushButton("Inverze", self)
        self._invers_button.setStyleSheet("background-color:#98c74c;"
                                          "border-style: outset;border-width:"
                                        " 2px;border-radius: 10px;border-color: beige;"
                                        "font: bold 14px;min-width: 10em;padding: 6px;")

        #Tlacitka - Rotace
        self._text_otoceni = QLabel()
        self._text_otoceni.setText('Otočení')
        self._text_otoceni.setAlignment(Qt.AlignCenter)
        self._mirror_button = QPushButton("Zrcadlení", self)
        self._mirror_button.setStyleSheet("background-color:#ff704d;"
                                          "border-style: outset;border-width:"
                                        " 2px;border-radius: 10px;border-color: beige;"
                                        "font: bold 14px;min-width: 10em;padding: 6px;")
        self._180_button = QPushButton("180°", self)
        self._180_button.setStyleSheet("background-color:#ff704d;"
                                          "border-style: outset;border-width:"
                                        " 2px;border-radius: 10px;border-color: beige;"
                                        "font: bold 14px;min-width: 10em;padding: 6px;")

        #Oblast zobrazení BMP
        self._image_label = QLabel()
        self._image_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #self._image_label.setScaledContents(True)

        #self._image_label.setFixedWidth(100)
        self._info_label = QLabel()

        #self._image = QPixmap('new.bmp')
        #self._label.setPixmap(self._image)
        #self.resize(self._image.width(),self._image.height())



        #AppLayout
        grid = QGridLayout()
        grid_2 = QVBoxLayout()
        grid.addLayout(grid_2,0,0)
        grid_2.addWidget(self._open_button)
        grid_2.addWidget(self._text_barvy)
        grid_2.addWidget(self._grayscale_button)
        grid_2.addWidget(self._invers_button)
        grid_2.addWidget(self._text_otoceni)
        grid_2.addWidget(self._mirror_button)
        grid_2.addWidget(self._180_button)

        grid.addWidget(self._image_label, 0,1)
        #layout_data.addStretch()
        grid.addWidget(self._info_label,0,2)



        self.setLayout(grid)
        self.setLayout(grid_2)

        #Prirazeni funkci tlacitkum
        self._open_button.clicked.connect(self.select)
        self._grayscale_button.clicked.connect(self.grayscale_filter)
        self._invers_button.clicked.connect(self.invert_filter)
        self._mirror_button.clicked.connect(self.mirror_rotation)
        self._180_button.clicked.connect(self.rotation180)

        #Chybove hlaseni



    def rotation180(self):
        try:
            input_image = Image.open(soubor).convert('RGB')
            input_pixels = input_image.load()

            # Create output image
            output_image = Image.new("RGB", input_image.size,'white')
            draw = ImageDraw.Draw(output_image)

            # Copy pixels
            for x in range(output_image.width):
                for y in range(output_image.height):
                    yp = input_image.height - y - 1
                    draw.point((x, y), input_pixels[x,yp])

            output_image.show()
            #output_image.save("output.bmp")
            return
        except Exception:
           print("Chyba")
           self._msgbox = QMessageBox()
           self._msgbox.setIcon(QMessageBox.Warning)
           self._msgbox.setText("Chyba! Není načten obrázek.")
           self._msgbox.exec()


    def mirror_rotation(self):
        try:
            input_image = Image.open(soubor).convert('RGB')
            input_pixels = input_image.load()

            # Create output image
            output_image = Image.new("RGB", input_image.size,'white')
            draw = ImageDraw.Draw(output_image)

            # Copy pixels
            for x in range(output_image.width):
                for y in range(output_image.height):
                    xp = input_image.width - x - 1
                    draw.point((x, y), input_pixels[xp, y])

            output_image.show()
            #output_image.save("output.bmp")
            return
        except Exception:
           print("Chyba")
           self._msgbox = QMessageBox()
           self._msgbox.setIcon(QMessageBox.Warning)
           self._msgbox.setText("Chyba! Není načten obrázek.")
           self._msgbox.exec()
            #return




    def invert_filter(self):
        try:
             def get_pixel(image, i, j):
                # Inside image bounds?
                width, height = image.size
                if i > width or j > height:
                  return None

                # Get Pixel
                pixel = image.getpixel((i, j))
                return pixel

             bmp = Image.open(soubor).convert('RGB')             #!!!!!!!!!!!!!
             width, height = bmp.size
             new = Image.new("RGB", (width, height), "white")
             pixels = new.load()
             for i in range(width):
                for j in range(height):
              # Get Pixel
                      pixel = get_pixel(bmp, i, j)

                      # Get R, G, B values (This are int from 0 to 255)
                      red =   pixel[0]
                      green = pixel[1]
                      blue =  pixel[2]

                      # Transform to grayscale
                      gray = (255-red) + (255-green) + (255-blue)

                      # Set Pixel in new image
                      pixels[i, j] = (int(gray), int(gray), int(gray))

             # Return new image
             new.show()
             return
        except Exception:
              print("Chyba")
              self._msgbox = QMessageBox()
              self._msgbox.setIcon(QMessageBox.Warning)
              self._msgbox.setText("Chyba! Není načten obrázek.")
              self._msgbox.exec()


    def grayscale_filter(self):
        try:
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
        except Exception:
              print("Chyba")
              self._msgbox = QMessageBox()
              self._msgbox.setIcon(QMessageBox.Warning)
              self._msgbox.setText("Chyba! Není načten obrázek.")
              self._msgbox.exec()


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
w.setStyleSheet("MainWindow {background: #cccccc;}")
w.setGeometry(500,500,500,200)
w.show()
sys.exit(app.exec())

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QFileDialog, QApplication

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
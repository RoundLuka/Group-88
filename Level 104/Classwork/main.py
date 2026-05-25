from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys

class Picture(QWidget):
    def __init__(self, img_url):
        super().__init__()

        self.setMinimumSize(400, 300)
        
        layout = QVBoxLayout(self)

        # 1. Create the QPixmap and load a file
        pixmap = QPixmap(img_url) 

        # 2. Create a label to hold the pixmap
        label = QLabel()
        label.setPixmap(pixmap)

        layout.addWidget(label)



def main():
    app = QApplication(sys.argv)
    window = Picture('Level 104\Classwork\image.png')
    window.show()
    sys.exit(app.exec_())

main()
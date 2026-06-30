from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys

class Window(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        x_position = 200
        y_position = 200

        width = 500
        height = 400
        
        self.setGeometry(x_position, y_position, width, height) # არგუმენტი: xPosition, yPosition, width, height
        self.setWindowTitle("Luka's program")
        self.window_content()

        
    def handle_click(self):
        self.myButton.setText("Button got clicked")
        self.myButton.adjustSize()

    def window_content(self):
        self.myText = QLabel(self)
        self.myText.setText("Hello my first python gui")
        self.myText.move(75, 50)

        self.myButton = QPushButton(self)
        self.myButton.setText("Click me")
        self.myButton.setGeometry(100, 0, 200, 100)

        self.myButton.clicked.connect(self.handle_click)

        self.myButton.setStyleSheet("""
            background-color: green;
            border: 1px solid black;
            font-size: 25px;
            padding: 10px;
        """)

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

main()






































# def window():
#     app = QApplication(sys.argv)
#     win1 = QMainWindow()

#     x_position = 200
#     y_position = 200

#     width = 500
#     height = 400
    
#     win1.setGeometry(x_position, y_position, width, height) # არგუმენტი: xPosition, yPosition, width, height
#     win1.setWindowTitle("Luka's program")

#     myText = QLabel(win1)
#     myText.setText("Hello my first python gui")
#     myText.move(75, 50)

#     myButton = QPushButton(win1)
#     myButton.setText("Click me")
#     myButton.setGeometry(100, 0, 200, 100)

#     myButton.clicked.connect(handle_click)

#     myButton.setStyleSheet("""
#         background-color: green;
#         border: 1px solid black;
#         font-size: 25px;
#         padding: 10px;
#     """)
    
#     win1.show() # გამოჩნდეს interface
#     sys.exit(app.exec_())

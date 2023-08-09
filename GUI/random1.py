import sys
from passwordgenerator import random_password_generator
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Password Generator")
        self.button =QPushButton("Generate")
        self.button.clicked.connect(self.the_button_was_clicked)


        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText(self.generate_random_password())
    
    def generate_random_password(self):
       self.generated_password = random_password_generator()
       return self.generated_password
        


app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()
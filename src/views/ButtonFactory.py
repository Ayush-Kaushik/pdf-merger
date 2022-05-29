from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ButtonFactory:
    def create_button(self, title: str, action) -> QPushButton:
        button = QPushButton()
        button.setText(title)
        button.clicked.connect(action)
        return button
# Author: Ayush Kaushik

from PyQt5.QtWidgets import QPushButton

class ButtonFactory:
    def create_button(self, title: str, action) -> QPushButton:
        button = QPushButton()
        button.setText(title)
        button.clicked.connect(action)
        return button
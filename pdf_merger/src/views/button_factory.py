# Author: Ayush Kaushik

from PyQt5.QtWidgets import QPushButton


class ButtonFactory:
    def create(self, title: str, action) -> QPushButton:
        button = QPushButton()
        button.setText(title)
        button.clicked.connect(action)
        return button

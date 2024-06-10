# Author: Ayush Kaushik

from PyQt5.QtWidgets import QPushButton


class ButtonFactory:

    @staticmethod
    def create(title: str, action) -> QPushButton:
        button = QPushButton()
        button.setText(title)
        button.clicked.connect(action)
        return button

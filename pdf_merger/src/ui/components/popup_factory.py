# Author: Ayush Kaushik

from PyQt5.QtWidgets import QMessageBox
from enum import Enum


class PopupType(Enum):
    INFO = "Info"
    ERROR = "Error"


class PopupFactory:
    @staticmethod
    def get(popup_type, message):
        try:
            if popup_type == PopupType.INFO:
                return InfoPopup(message)
            if popup_type == PopupType.ERROR:
                return ErrorPopup(message)
            raise AssertionError("Popup type not found")
        except AssertionError as exception:
            print(exception)


class InfoPopup(QMessageBox):
    def __init__(self, message):
        super().__init__()
        self.setText(message)
        self.setIcon(QMessageBox.Information)


class ErrorPopup(QMessageBox):
    def __init__(self, message):
        super().__init__()
        self.setText(message)
        self.setIcon(QMessageBox.Critical)

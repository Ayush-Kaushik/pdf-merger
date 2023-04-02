# Author: Ayush Kaushik

from PyQt5.QtWidgets import QMessageBox

class PopupFactory():
    @staticmethod
    def getPopup(popupType, message):
        try:
            if popupType == "Info":
                return InfoPopup(message)
            if popupType == "Error":
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

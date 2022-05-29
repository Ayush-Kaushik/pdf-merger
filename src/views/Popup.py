from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Popup(QMessageBox):
    msg = QMessageBox()

class InfoPopup(Popup):
    print("info popup")

class ErrorPopup(Popup):
    print("Error popup")

import sys
from PyPDF2 import PdfFileMerger as pdfM
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#
# Class deals with operations related to pdf creation
#
#
class PDFCollection():
    def __init__(self):
        self.pdfCollection = []

    def mergePDFQueue(self):
        self.pdfCollection = []

    def clearPDFQueue(self):
        self.pdfCollection = []

    def setPDFQueue(self):
        self.pdfCollection = []
        
    def setOutputLocation():
        self.pdfCollection = []

#
# List Widget Box which accepts multiple PDF files
#


class DragAndDropArea(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            print(event.mimeData().urls())
        else:
            event.ignore()

#
# Create a window with width that matches the width of the screen
# On top, have a input box that is disabled but only displays the location of
# where the file will be saved
#
# In the middle will be a list of pdf's that can be dragged and dropped
# Also, it can be reordered
#
# At the bottom, we have two button
# One to merge, second to clear all the input fields including dialog box
#


class MergerApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PDF Merger'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 400
        self.initUI()
        self.widget = QWidget()

    def findOutputLocation(self):
        directory = QFileDialog.getExistingDirectory(
            None, "Choose Directory", "")
        savedLocation = ""
        if directory != "":
            savedLocation = directory + "/merged.pdf"
        self.textbox.setText(savedLocation)

    def setScreenDimensions(self):
        screen = app.primaryScreen()
        size = screen.size()
        self.width = size.width()

    def initUI(self):
        self.setScreenDimensions()
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Input box that shows location of merged file
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize((self.width - 200), 40)

        # Button to open dialog to select location to place merged file
        self.button = QPushButton(self)
        self.button.setText("Press")
        self.button.clicked.connect(self.findOutputLocation)
        self.button.move(20, 40)

        # PDF drag and drop area
        self.dragAndDropView = DragAndDropArea(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MergerApp()
    sys.exit(app.exec_())

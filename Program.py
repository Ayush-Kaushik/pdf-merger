import sys, os
from PyPDF2 import PdfFileMerger
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# Class deals with operations related to pdf creation
class PDFCollection():
    pdfRouteCollection = []
    merger = PdfFileMerger()
    targetPDFLocation = ""

    def mergePDFQueue(self):
        for file in PDFCollection.pdfRouteCollection:
            PDFCollection.merger.append(file)
        PDFCollection.merger.write(PDFCollection.targetPDFLocation)
            
    def clearPDFQueue(self):
        PDFCollection.pdfRouteCollection = []

    def appendToPDFQueue(self, item):
        PDFCollection.pdfRouteCollection.append(item)

    def setOutputLocation(self, outputLocation):
        PDFCollection.targetPDFLocation = outputLocation

# List Widget Box which accepts multiple PDF files
class DragAndDropArea(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)

    def clearQueue(self):
        self.clear()

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

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    if url.toString().endswith(".pdf"):
                        PDFCollection.pdfRouteCollection.append(str(url.toLocalFile()))
                        self.addItem(str(url.toLocalFile()))
        else:
            event.ignore()


# Create a window with width that matches the width of the screen
# On top, have a input box that is disabled but only displays the location of
# where the file will be saved
#
# In the middle will be a list of pdf's that can be dragged and dropped
# Also, it can be reordered
#
# At the bottom, we have two button
# One to merge, second to clear all the input fields including dialog box
class MergerApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PDF Merger'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 400
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.initUI()
        layout = QHBoxLayout()
        self.widget.setLayout(layout)
        self.pdfCollection = PDFCollection()

    def findOutputLocation(self):
        directory = QFileDialog.getExistingDirectory(
            None, "Choose Directory", "")
        savedLocation = ""
        if directory != "":
            savedLocation = directory + "/merged.pdf"
            self.pdfCollection.setOutputLocation(savedLocation)
        self.textbox.setText(savedLocation)

    def resetApp(self):
        self.pdfCollection.pdfCollection = []
        self.pdfCollection.targetPDFLocation = ""
        self.textbox.setText(self.pdfCollection.targetPDFLocation)
        self.pdfCollection.clearPDFQueue()
        self.dragAndDropView.clearQueue()
        
    def mergePDF(self):
        PDFCollection.mergePDFQueue(self)
        self.resetApp()

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
        self.textbox.resize((self.width - 200), 40)

        # Button to open dialog to select location to place merged file
        self.button = QPushButton(self)
        self.button.setText("Save To")
        self.button.clicked.connect(self.findOutputLocation)

        # PDF drag and drop area
        self.dragAndDropView = DragAndDropArea(self)

        # Call To Action Buttons
        self.deleteButton = QPushButton(self)
        self.deleteButton.setText("Reset")
        self.deleteButton.clicked.connect(self.resetApp)

        self.mergeButton = QPushButton(self)
        self.mergeButton.setText("Merge")
        self.mergeButton.clicked.connect(self.mergePDF)

        # Setup their layouts
        self.verticalLayout = QVBoxLayout()

        self.horizontalBoyLayout = QHBoxLayout()
        self.horizontalBoyLayout.addWidget(self.textbox, 2)
        self.horizontalBoyLayout.addWidget(self.button, 0)

        self.dragAndDropAreaLayout = QHBoxLayout()
        self.dragAndDropAreaLayout.addWidget(self.dragAndDropView)

        self.callToActionLayout = QHBoxLayout()
        self.callToActionLayout.addWidget(self.deleteButton, 1)
        self.callToActionLayout.addWidget(self.mergeButton, 1)

        self.verticalLayout.addLayout(self.horizontalBoyLayout)
        self.verticalLayout.addLayout(self.dragAndDropAreaLayout)
        self.verticalLayout.addLayout(self.callToActionLayout)

        self.widget.setLayout(self.verticalLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MergerApp()
    sys.exit(app.exec_())

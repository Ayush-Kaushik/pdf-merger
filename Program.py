import sys, os
from unicodedata import numeric
from PyPDF2 import PdfFileMerger
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Deals with operations related to pdf creation
class PDFService:
    def __init__(self, merger: PdfFileMerger, pdfFilePathCollection, targetFilePath: str):
        self.merger = merger
        self.filePathList = pdfFilePathCollection
        self.targetFilePath = targetFilePath
        
    def mergePDFQueue(self):
        for file in self.filePathList:
            self.merger.append(file)
        self.merger.write(self.targetFilePath)
            
    def clearPDFQueue(self):
        self.filePathList = []

    def appendToPDFQueue(self, item: str):
        self.filePathList.append(item)

    def setTargetFilePath(self, filePath):
        self.targetFilePath = filePath
        
    def getTargetFilePath(self):
        return self.targetFilePath
    
    def getFilePathList(self):
        return self.filePathList

# List Widget Box which accepts multiple PDF files
class DragAndDropArea(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)
        self.pdfService = pdfService
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
    
    def clearQueue(self):
        self.clear()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            return super().dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            return super().dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    if url.toString().endswith(".pdf"):
                        self.pdfService.filePathList.append(str(url.toLocalFile()))
                        self.addItem(str(url.toLocalFile()))
        else:
            return super().dropEvent(event)


class AppLayoutConfig:
    def __init__(self, title: str, left: int, top: int, height: int, width: int):
        self.title = title
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        
class Labels:
    CHOOSE_DIRECTORY = "Choose Directory"
    SAVE_TO = "Save To.."
    RESET = "RESET"
    MERGE = "Merge"

class ButtonFactory:
    def create_button(self, title: str, action) -> QPushButton:
        button = QPushButton(self)
        button.setText(title)
        button.clicked.connect(action)
        return button

class MergerApp(QMainWindow):
    def __init__(self, pdfService: PDFService, config: AppLayoutConfig, labels: Labels):
        super().__init__()
        self.config = config 
        self.pdfService = pdfService
        self.labels = labels 
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.initializeAppUI()
        self.widget.setLayout(QHBoxLayout())
        
    def getOutputFilePath(self) -> str:
        directory = QFileDialog.getExistingDirectory(
            None, labels.CHOOSE_DIRECTORY, "")
        savedLocation = ""
        if directory != "":
            savedLocation = directory + "/merged.pdf"        
            self.pdfService.setTargetFilePath(savedLocation)
        self.textbox.setText(savedLocation)

    def resetApp(self):
        self.pdfService.setTargetFilePath("")
        self.textbox.setText(self.pdfService.targetFilePath)
        self.pdfService.clearPDFQueue()
        self.dragAndDropView.clearQueue()
    
    # return location of merged pdf if successful
    # otherwise return null
    def mergePDF(self):
        try:
            self.pdfService.mergePDFQueue()
        except Exception as exception:
            print(exception)
        finally:
            self.resetApp()

    def initializeAppUI(self):
        self.setWindowTitle(self.config.title)
        self.setGeometry(self.config.left, self.config.top, self.config.width, self.config.height)

        # Input box that shows location of merged file
        self.textbox = QLineEdit(self)
        self.textbox.resize((self.config.width - 200), 40)

        # Button to open dialog to select location to place merged file
        self.saveButton = ButtonFactory.create_button(self, "Save To", self.getOutputFilePath)
        self.deleteButton = ButtonFactory.create_button(self, "Reset", self.resetApp)
        self.mergeButton = ButtonFactory.create_button(self, "Merge", self.mergePDF)

        # PDF drag and drop area
        self.dragAndDropView = DragAndDropArea(self)

        # Setup their layouts
        self.verticalLayout = QVBoxLayout()

        self.horizontalBoyLayout = QHBoxLayout()
        self.horizontalBoyLayout.addWidget(self.textbox, 2)
        self.horizontalBoyLayout.addWidget(self.saveButton, 0)

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
    
    pdfService = PDFService(PdfFileMerger(), [], "")
    appConfig = AppLayoutConfig("PDF Merger", 10, 10, 500, 400)
    labels = Labels()
    
    ex = MergerApp(pdfService, appConfig, labels)
    sys.exit(app.exec_())

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.services.PDFService import PDFService

# List Widget Box which accepts multiple PDF files
class DragAndDropArea(QListWidget):
    
    '''
    Using polymorphism here to be able to pass any services
    PDFService, ImageService etc.
    '''
    def __init__(self, mediaService, parent=None):
        super().__init__(parent)
        
        self.setAcceptDrops(True)
        self.resize(600, 600)
        self.service = mediaService
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
                    for ext in self.service.VALID_EXTENSIONS:
                        if url.toString().endswith(ext):
                            self.service.appendToQueue(url)
                            self.addItem(str(url.toLocalFile()))
   
        else:
            return super().dropEvent(event)
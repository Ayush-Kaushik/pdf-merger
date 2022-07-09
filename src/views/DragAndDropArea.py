# Author: Ayush Kaushik

import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QListWidget
from src.exceptions.InvalidExtensionError import InvalidExtensionError
from src.views.PopupFactory import PopupFactory

class DragAndDropArea(QListWidget):

    '''
    List Widget Box which accepts multiple PDF files
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

            try:
                for url in event.mimeData().urls():
                    if url.isLocalFile():
                        filename, file_extension = os.path.splitext(url.toString())                     
                        if file_extension in self.service.VALID_EXTENSIONS:
                            self.service.appendToQueue(url)
                            self.addItem(str(url.toLocalFile()))
                        else:
                            raise InvalidExtensionError(
                                self.service.VALID_EXTENSIONS)
            except InvalidExtensionError as invalidExtensionException:
                popup = PopupFactory.getPopup(
                    "Error", invalidExtensionException.message)
                popup.exec_()
        else:
            return super().dropEvent(event)

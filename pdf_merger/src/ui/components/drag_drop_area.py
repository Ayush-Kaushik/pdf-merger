# Author: Ayush Kaushik

import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QListWidget
from pdf_merger.src.exceptions import InvalidExtensionError
from pdf_merger.src.ui.components.popup_factory import PopupFactory
from pdf_merger.src.services.abstract_file_merger_service import AbstractFileMergerService

'''
    List Widget Box which accepts multiple files
    
    Using polymorphism here to be able to pass any services
    PDFService, ImageService etc.
'''


class DragAndDropArea(QListWidget):
    def __init__(self, service: AbstractFileMergerService, parent=None):
        super().__init__(parent)

        self.setAcceptDrops(True)
        self.resize(600, 600)
        self.service = service
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def clear_area(self):
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
                        if file_extension in self.service.allowed_file_extensions:
                            self.service.append_file(url)
                            self.addItem(str(url.toLocalFile()))
                        else:
                            raise InvalidExtensionError(
                                self.service.allowed_file_extensions)
            except InvalidExtensionError as invalidExtensionException:
                popup = PopupFactory.get("Error", invalidExtensionException.message)
                popup.exec_()
        else:
            return super().dropEvent(event)

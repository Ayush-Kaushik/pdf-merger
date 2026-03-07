from pathlib import Path
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QFileDialog, QListWidget,
    QListWidgetItem
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont

from .file_item_widget import FileItemWidget

class FileUploadZone(QWidget):
    filesSelected = pyqtSignal(list)

    def __init__(self, accept_extensions: list, mode: str = "pdf"):
        super().__init__()
        self.accept_extensions = accept_extensions
        self.mode = mode
        self.selected_files = []

        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        self.setLayout(layout)

        # Instruction label (clickable)
        self.instruction_label = QLabel(
            f"Drag and drop files below or click here to browse ({', '.join(self.accept_extensions)})"
        )
        self.instruction_label.setAlignment(Qt.AlignLeft)
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)
        self.instruction_label.setFont(font)
        layout.addWidget(self.instruction_label)
        self.instruction_label.mousePressEvent = lambda _: self.open_file_dialog()

        # File list widget with internal move
        self.file_list_widget = QListWidget()
        self.file_list_widget.setDragDropMode(QListWidget.InternalMove)
        self.file_list_widget.setSelectionMode(QListWidget.NoSelection)  # prevent selection box
        self.file_list_widget.model().rowsMoved.connect(self._emit_files_changed)
        layout.addWidget(self.file_list_widget)

    # -----------------------
    # File dialog
    # -----------------------
    def open_file_dialog(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Files",
            "",
            "Files ({})".format(" ".join(f"*{ext}" for ext in self.accept_extensions))
        )
        if files:
            self._handle_files(files)

    # -----------------------
    # Drag & Drop
    # -----------------------
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        files = [url.toLocalFile() for url in urls]
        self._handle_files(files)

    # -----------------------
    # Handle files
    # -----------------------
    def _handle_files(self, files):
        for file_path in files:
            if not any(file_path.lower().endswith(ext) for ext in self.accept_extensions):
                continue
            if file_path not in self.selected_files:
                self.selected_files.append(file_path)
                self._add_file_item(file_path)

        self.filesSelected.emit(self.selected_files)

    def _add_file_item(self, file_path):
        list_item = QListWidgetItem()
        file_widget = FileItemWidget(file_path, remove_callback=self._remove_file_by_path)
        list_item.setSizeHint(file_widget.sizeHint())
        self.file_list_widget.addItem(list_item)
        self.file_list_widget.setItemWidget(list_item, file_widget)

    def _remove_file_by_path(self, file_path):
        for i in range(self.file_list_widget.count()):
            item = self.file_list_widget.item(i)
            widget = self.file_list_widget.itemWidget(item)
            if widget.file_path == file_path:
                self.selected_files.remove(file_path)
                self.file_list_widget.takeItem(i)
                self.filesSelected.emit(self.selected_files)
                break

    def clear_area(self):
        self.selected_files.clear()
        self.file_list_widget.clear()
        self.filesSelected.emit(self.selected_files)

    # -----------------------
    # Emit files after reorder
    # -----------------------
    def _emit_files_changed(self, *args):
        # reorder selected_files according to the QListWidget order
        new_order = []
        for i in range(self.file_list_widget.count()):
            item_widget = self.file_list_widget.itemWidget(self.file_list_widget.item(i))
            name_label = item_widget.layout().itemAt(0).widget()
            full_path = next((f for f in self.selected_files if Path(f).name == name_label.text()), None)
            if full_path:
                new_order.append(full_path)
        self.selected_files = new_order
        self.filesSelected.emit(self.selected_files)
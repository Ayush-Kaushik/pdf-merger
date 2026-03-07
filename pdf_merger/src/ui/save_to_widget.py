from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal, Qt
import os

class SaveToWidget(QWidget):
    pathSelected = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_path = ""

        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)
        self.setLayout(layout)

        # Label
        self.label = QLabel("Save Merged File To:")
        font = QFont()
        font.setBold(True)
        font.setPointSize(11)
        self.label.setFont(font)
        layout.addWidget(self.label)

        # Horizontal input + button
        h_layout = QHBoxLayout()
        h_layout.setSpacing(5)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Location of merged file")
        self.input_field.setMinimumHeight(28)
        self.input_field.setStyleSheet("""
            QLineEdit {
                border: 1px solid #d1d5db;
                border-radius: 6px;
                padding-left: 6px;
            }
            QLineEdit:focus {
                border: 1px solid #3b82f6;
            }
        """)

        self.browse_btn = QPushButton("Browse…")
        self.browse_btn.setFixedHeight(28)
        self.browse_btn.setStyleSheet("""
            QPushButton {
                background-color: #3b82f6;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 0 12px;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
        """)

        h_layout.addWidget(self.input_field)
        h_layout.addWidget(self.browse_btn)
        layout.addLayout(h_layout)

        # Set border around the save area
        self.setStyleSheet("""
            QWidget {
                border: 1px solid #d1d5db;
                background-color: #f9fafb;
                border-radius: 8px;
                padding: 8px;
            }
            QWidget:hover {
                background-color: #f3f4f6;
            }
        """)

        # Connections
        self.browse_btn.clicked.connect(self._open_file_dialog)

    def _open_file_dialog(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Select Save Location", "", "PDF Files (*.pdf);;All Files (*)"
        )
        if file_path:
            self.selected_path = file_path
            self.input_field.setText(file_path)
            self.pathSelected.emit(file_path)

    def set_path(self, path: str):
        self.selected_path = path
        self.input_field.setText(path)

    def get_path(self) -> str:
        return self.selected_path

    def clear(self):
        self.selected_path = ""
        self.input_field.clear()
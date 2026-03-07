from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class FileItemWidget(QWidget):
    """Custom widget for each file entry with border, info, remove button."""

    def __init__(self, file_path: str, remove_callback):
        super().__init__()
        self.file_path = file_path
        layout = QHBoxLayout()
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(5)
        self.setLayout(layout)

        # Border style
        self.setStyleSheet("""
            QWidget {
                border: 1px solid #d1d5db;
                background-color: #f9fafb;
            }
            QWidget:hover {
                background-color: #f3f4f6;
            }
        """)

        # File name
        name_label = QLabel(file_path.split('/')[-1])
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        name_label.setFont(font)
        layout.addWidget(name_label)

        # Info icon
        info_label = QLabel("i")
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setFixedSize(18, 18)
        info_label.setStyleSheet("""
            QLabel {
                background-color: #3b82f6;
                color: white;
                border-radius: 9px;
                font-weight: bold;
                font-size: 12px;
            }
        """)
        layout.addWidget(info_label)

        layout.addStretch()

        # Remove button
        remove_btn = QPushButton("✕")
        remove_btn.setFixedSize(20, 20)
        remove_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff5c5c;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover { background-color: #ff1f1f; }
        """)
        layout.addWidget(remove_btn)
        remove_btn.clicked.connect(lambda: remove_callback(self.file_path))

    # Ensure mouse events pass through for drag
    def mousePressEvent(self, event):
        event.ignore()
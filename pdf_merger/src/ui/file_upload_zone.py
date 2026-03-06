from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont

class FileUploadZone(QWidget):
    filesSelected = pyqtSignal(list)

    def __init__(self, accept: str, mode: str = "pdf"):
        super().__init__()

        self.accept = accept
        self.mode = mode
        self.selected_files = []

        self.setObjectName("uploadZone")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setAcceptDrops(True)
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(200)

        self._init_ui()
        self._apply_style()

    def _init_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.icon_label = QLabel("⬆")
        self.icon_label.setFont(QFont("Arial", 28))
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.main_label = QLabel(
            f"Drop {'PDF files' if self.mode == 'pdf' else 'files'} here or click to browse"
        )
        self.main_label.setAlignment(Qt.AlignCenter)
        main_font = QFont()
        main_font.setPointSize(14)   # Bigger
        main_font.setBold(True)      # Bold
        self.main_label.setFont(main_font)

        self.sub_label = QLabel("Supports: PDF files")
        self.sub_label.setAlignment(Qt.AlignCenter)
        self.sub_label.setStyleSheet("color: gray; font-size: 12px;")

        layout.addWidget(self.icon_label)
        layout.addWidget(self.main_label)
        layout.addWidget(self.sub_label)

        self.setLayout(layout)

    def _apply_style(self):
        self.setStyleSheet("""
            QWidget#uploadZone {
                border: 2px dashed #d1d5db;
                border-radius: 12px;
                padding: 30px;
                background-color: white;
            }

            QWidget#uploadZone:hover {
                border-color: #60a5fa;
                background-color: #f8fafc;
            }
        """)

    # -----------------------
    # File dialog
    # -----------------------
    def mousePressEvent(self, _):
        self.open_file_dialog()

    def open_file_dialog(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Files",
            "",
            self.accept
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
    # Internal handler
    # -----------------------
    def _handle_files(self, files):
        valid_files = []

        for file in files:
            if file.lower().endswith(".pdf"):
                valid_files.append(file)

        if valid_files:
            self.selected_files.extend(valid_files)
            self.filesSelected.emit(valid_files)

    def clear_area(self):
        self.selected_files.clear()
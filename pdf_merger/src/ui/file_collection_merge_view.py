# Author: Ayush Kaushik

from pathlib import Path
from PyQt5.QtWidgets import (
    QWidget,
    QFileDialog,
    QVBoxLayout,
    QLineEdit,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QComboBox
)
from PyQt5.QtCore import Qt
from pdf_merger.src.ui.file_upload_zone import FileUploadZone
from pdf_merger.src.ui.constants import Labels

class FileCollectionMergeView(QWidget):
    def __init__(self, service=None, config=None, labels: Labels = None):
        super().__init__()

        self.fileMergerService = service
        self.config = config
        self.labels = labels

        self.text_box = None
        self.save_button = None
        self.drag_drop_view = None
        self.page_size_combo = None
        self.page_size_info_label = None

        self.initialize_layout()

    # ---------------------------------------------------------
    # FILE HANDLING
    # ---------------------------------------------------------

    def handle_selected_files(self, files):
        for file in files:
            self.fileMergerService.add_file(Path(file))

    # ---------------------------------------------------------
    # OUTPUT DIRECTORY
    # ---------------------------------------------------------

    def get_output_file_path(self):
        directory = QFileDialog.getExistingDirectory(self, self.labels.CHOOSE_DIRECTORY, "")
        if directory:
            save_file_path = f"{directory}/merged.pdf"
            self.fileMergerService.set_output_target(Path(save_file_path))
            self.text_box.setText(save_file_path)

    # ---------------------------------------------------------
    # RESET
    # ---------------------------------------------------------

    def reset_widget(self):
        self.fileMergerService.set_output_target(Path())
        self.fileMergerService.clear_list()
        self.text_box.clear()
        self.drag_drop_view.clear_area()
        if self.page_size_combo:
            self.page_size_combo.setCurrentIndex(0)
        if self.page_size_info_label:
            self.page_size_info_label.setText(
                "Keep the original page sizes or adjust pages to a standard size."
            )

    # ---------------------------------------------------------
    # MERGE
    # ---------------------------------------------------------

    def merge_files(self):
        page_size_option = self.page_size_combo.currentText() if self.page_size_combo else "Keep Original Sizes"
        if self.fileMergerService.merge_files(page_size_option):
            popup = QMessageBox(QMessageBox.Information, "Task Successful!", "PDF files merged successfully.")
            popup.exec_()
            self.reset_widget()
        else:
            popup = QMessageBox(QMessageBox.Critical, "Task Failed!", "Failed to merge PDF files.")
            popup.exec_()

    # ---------------------------------------------------------
    # UI LAYOUT
    # ---------------------------------------------------------

    def initialize_layout(self):
        # ---------------- Output row ----------------
        self.text_box = QLineEdit()
        self.text_box.setDisabled(True)
        self.text_box.setFixedHeight(40)

        self.save_button = QPushButton(self.labels.SAVE_TO)
        self.save_button.setFixedHeight(45)
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: #3b82f6;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border-radius: 8px;
            }
            QPushButton:hover { background-color: #2563eb; }
            QPushButton:pressed { background-color: #1d4ed8; }
        """)
        self.save_button.clicked.connect(self.get_output_file_path)

        horizontal_box_layout = QHBoxLayout()
        horizontal_box_layout.addWidget(self.text_box, 2)
        horizontal_box_layout.addWidget(self.save_button, 1)

        # ---------------- File Upload ----------------
        self.drag_drop_view = FileUploadZone(accept="PDF Files (*.pdf)", multiple=True, mode="pdf")
        self.drag_drop_view.filesSelected.connect(self.handle_selected_files)

        # ---------------- Page Size Handling ----------------
        page_size_label = QLabel("Page Size Handling:")
        page_size_label.setStyleSheet("font-weight: bold; font-size: 12px;")
        self.page_size_combo = QComboBox()
        self.page_size_combo.addItems([
            "Keep Original Sizes",
            "Resize / Stretch to Standard",
            "Fit Content Proportionally"
        ])
        self.page_size_combo.setStyleSheet("""
            QComboBox {
                font-size: 13px;
                padding: 5px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
            }
        """)
        self.page_size_combo.currentIndexChanged.connect(self.update_page_size_info)

        self.page_size_info_label = QLabel(
            "Keep the original page sizes or adjust pages to a standard size."
        )
        self.page_size_info_label.setStyleSheet("font-size: 11px; color: #6b7280;")
        self.page_size_info_label.setWordWrap(True)
        self.page_size_info_label.setAlignment(Qt.AlignLeft)

        page_size_layout = QVBoxLayout()
        page_size_layout.addWidget(page_size_label)
        page_size_layout.addWidget(self.page_size_combo)
        page_size_layout.addWidget(self.page_size_info_label)

        # ---------------- Bottom Buttons ----------------
        delete_button = QPushButton(self.labels.RESET)
        delete_button.setFixedHeight(45)
        delete_button.setStyleSheet("""
            QPushButton { background-color: #ef4444; color: white; font-weight: bold; font-size: 14px; border-radius: 8px; }
            QPushButton:hover { background-color: #dc2626; }
            QPushButton:pressed { background-color: #b91c1c; }
        """)
        delete_button.clicked.connect(self.reset_widget)

        merge_button = QPushButton(self.labels.MERGE)
        merge_button.setFixedHeight(45)
        merge_button.setStyleSheet("""
            QPushButton { background-color: #22c55e; color: white; font-weight: bold; font-size: 14px; border-radius: 8px; }
            QPushButton:hover { background-color: #16a34a; }
            QPushButton:pressed { background-color: #15803d; }
        """)
        merge_button.clicked.connect(self.merge_files)

        call_to_action_layout = QHBoxLayout()
        call_to_action_layout.addWidget(delete_button)
        call_to_action_layout.addWidget(merge_button)

        # ---------------- Main Layout ----------------
        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(horizontal_box_layout)
        vertical_layout.addWidget(self.drag_drop_view)
        vertical_layout.addLayout(page_size_layout)
        vertical_layout.addLayout(call_to_action_layout)

        self.setLayout(vertical_layout)

    # ---------------------------------------------------------
    # PAGE SIZE INFO UPDATE
    # ---------------------------------------------------------

    def update_page_size_info(self):
        option = self.page_size_combo.currentText()
        if option == "Keep Original Sizes":
            text = "Pages will keep their original sizes; merged PDF may have mixed page sizes."
        elif option == "Resize / Stretch to Standard":
            text = "All pages will be resized to a standard size; content may stretch."
        elif option == "Fit Content Proportionally":
            text = "All pages will fit a standard size proportionally; aspect ratio preserved; may add margins."
        else:
            text = ""
        self.page_size_info_label.setText(text)

    # ---------------------------------------------------------

    def get_widget(self):
        return self
# Author: Ayush Kaushik

from pathlib import Path
from PyQt5.QtWidgets import (
    QWidget,
    QFileDialog,
    QVBoxLayout,
    QLineEdit,
    QHBoxLayout,
    QMessageBox,
    QPushButton
)

from pdf_merger.src.data.merge_job import MergeJob
from pdf_merger.src.services.image_merger_service import ImageMergerService
from pdf_merger.src.services.pdf_merger_service import PdfMergerService
from pdf_merger.src.ui.file_upload_zone import FileUploadZone
from pdf_merger.src.ui.constants import Labels

class FileCollectionMergeView(QWidget):
    def __init__(self, service: PdfMergerService |  ImageMergerService, labels: Labels = None, accepted_file_types: str = "", mode: str = ""):
        super().__init__()

        self.fileMergerService = service
        self.merge_job = MergeJob()
        self.labels = labels
        self.accepted_file_types = accepted_file_types
        self.mode = mode

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
            self.merge_job.add_file(Path(file))

    # ---------------------------------------------------------
    # OUTPUT DIRECTORY
    # ---------------------------------------------------------

    def get_output_file_path(self):
        directory = QFileDialog.getExistingDirectory(self, self.labels.CHOOSE_DIRECTORY, "")
        if directory:
            save_file_path = f"{directory}/merged.pdf"
            self.merge_job.set_output_target(Path(save_file_path))
            self.text_box.setText(save_file_path)

    # ---------------------------------------------------------
    # RESET
    # ---------------------------------------------------------

    def reset_widget(self):
        self.merge_job.set_output_target(Path())
        self.merge_job.clear_list()
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
        self.drag_drop_view = FileUploadZone(accept=self.accepted_file_types, mode=self.mode)
        self.drag_drop_view.filesSelected.connect(self.handle_selected_files)

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
        vertical_layout.addLayout(call_to_action_layout)

        self.setLayout(vertical_layout)

    def get_widget(self):
        return self
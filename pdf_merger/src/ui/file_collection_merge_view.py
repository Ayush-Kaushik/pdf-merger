# Author: Ayush Kaushik

from pathlib import Path
from PyQt5.QtWidgets import (
    QWidget,
    QFileDialog,
    QVBoxLayout,
    QLineEdit,
    QHBoxLayout,
    QMessageBox,
    QPushButton,
    QFrame
)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont

from pdf_merger.src.ui.file_upload_zone import FileUploadZone
from pdf_merger.src.ui.constants import Labels


class FileCollectionMergeView(QWidget):
    """
    Generic view for operations that merge collections of files.
    This view contains NO business logic.
    """

    filesSelected = pyqtSignal(list)
    outputSelected = pyqtSignal(Path)
    mergeRequested = pyqtSignal()
    resetRequested = pyqtSignal()

    def __init__(
        self,
        labels: Labels,
        accepted_file_types: str = "",
        accept_extensions: list[str] = None,
        mode: str = ""
    ):
        super().__init__()

        self.labels = labels
        self.accepted_file_types = accepted_file_types
        self.accept_extensions = accept_extensions
        self.mode = mode

        self.output_path_box: QLineEdit | None = None
        self.drag_drop_view: FileUploadZone | None = None
        self.reset_button: QPushButton | None = None

        self._initialize_layout()

    # -------------------------
    # FILE HANDLING
    # -------------------------
    def _handle_selected_files(self, files: list[str]):
        """Forward file selection to controller and show reset button."""
        paths = [Path(file) for file in files]
        self.filesSelected.emit(paths)

        # Show reset button if files exist, hide if empty
        self.reset_button.setVisible(bool(files))

    # -------------------------
    # OUTPUT DIRECTORY
    # -------------------------
    def _select_output_directory(self):
        directory = QFileDialog.getExistingDirectory(
            self,
            self.labels.CHOOSE_DIRECTORY,
            ""
        )

        if not directory:
            return

        output_path = Path(directory) / "merged.pdf"
        self.output_path_box.setText(str(output_path))
        self.outputSelected.emit(output_path)

    # -------------------------
    # RESET VIEW
    # -------------------------
    def reset_view(self):
        """Clear visual state only."""
        self.output_path_box.clear()
        self.drag_drop_view.clear_area()
        self.reset_button.setVisible(False)

    # -------------------------
    # RESULT FEEDBACK
    # -------------------------
    def show_success(self, message: str):
        QMessageBox.information(self, "Success", message)

    def show_failure(self, message: str):
        QMessageBox.critical(self, "Error", message)

    # -------------------------
    # UI LAYOUT
    # -------------------------
    def _initialize_layout(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # -------- Save-To Area --------
        save_frame = QFrame()
        save_frame.setFrameShape(QFrame.StyledPanel)
        save_frame.setStyleSheet("""
            QFrame {
                border: 1px solid #d1d5db;
                border-radius: 8px;
                background-color: #fefefe;
            }
        """)
        save_layout = QHBoxLayout()
        save_layout.setContentsMargins(10, 10, 10, 10)
        save_layout.setSpacing(10)

        self.output_path_box = QLineEdit()
        self.output_path_box.setPlaceholderText("Select folder for saving merged file")
        self.output_path_box.setFixedHeight(40)
        self.output_path_box.setFont(QFont("", 11))
        self.output_path_box.setDisabled(True)

        self.save_button = QPushButton(self.labels.SAVE_TO)
        self.save_button.setFixedHeight(40)
        self.save_button.clicked.connect(self._select_output_directory)

        save_layout.addWidget(self.save_button, 1)
        save_layout.addWidget(self.output_path_box, 2)
        save_frame.setLayout(save_layout)
        layout.addWidget(save_frame)

        # -------- File Upload / Drag & Drop --------
        self.drag_drop_view = FileUploadZone(
            accept_extensions=self.accept_extensions,
            mode=self.mode
        )
        self.drag_drop_view.filesSelected.connect(self._handle_selected_files)

        # Reset button on top-right inside drag-drop
        self.reset_button = QPushButton(self.labels.RESET)
        self.reset_button.setFixedSize(80, 30)
        self.reset_button.setVisible(False)  # hide initially
        self.reset_button.clicked.connect(self.resetRequested.emit)

        # Overlay layout for label + reset button
        top_row = QHBoxLayout()
        top_row.addWidget(self.drag_drop_view.instruction_label, alignment=Qt.AlignLeft)
        top_row.addWidget(self.reset_button, alignment=Qt.AlignRight)
        top_row.setContentsMargins(5, 5, 5, 0)

        # Final layout combining top row + drag-drop area
        drag_drop_layout = QVBoxLayout()
        drag_drop_layout.addLayout(top_row)
        drag_drop_layout.addWidget(self.drag_drop_view)

        drag_drop_container = QFrame()
        drag_drop_container.setLayout(drag_drop_layout)
        drag_drop_container.setFrameShape(QFrame.StyledPanel)
        drag_drop_container.setStyleSheet("""
            QFrame {
                border: 1px solid #d1d5db;
                border-radius: 8px;
                background-color: #fefefe;
            }
        """)

        layout.addWidget(drag_drop_container)

        # -------- Merge Button --------
        merge_button = QPushButton(self.labels.MERGE)
        merge_button.setFixedHeight(45)
        merge_button.clicked.connect(self.mergeRequested.emit)
        layout.addWidget(merge_button)

        self.setLayout(layout)

    # -------------------------
    # COMPATIBILITY
    # -------------------------
    def get_widget(self):
        return self
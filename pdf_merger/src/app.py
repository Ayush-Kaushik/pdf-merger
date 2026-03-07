# Author: Ayush Kaushik

import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QVBoxLayout,
    QStackedWidget,
    QAction,
    QMessageBox,
    QLabel,
    QPushButton
)

from PyQt5.QtCore import Qt

from pdf_merger.src.services.image_merger_service import ImageMergerService
from pdf_merger.src.services.pdf_merger_service import PdfMergerService

from pdf_merger.src.ui.themes.theme_provider import ThemeProvider
from pdf_merger.src.ui.view_aggregator import ViewAggregator
from pdf_merger.src.ui.constants import Labels, LayoutConfig


class WelcomeView(QWidget):
    """Simple welcome screen with operation shortcuts."""

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("PDF Merger")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 28px; font-weight: bold;")

        subtitle = QLabel("Choose an operation to begin")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 14px; color: gray;")

        self.merge_pdf_btn = QPushButton("Merge PDFs")
        self.image_to_pdf_btn = QPushButton("Images → PDF")

        self.merge_pdf_btn.setMinimumHeight(40)
        self.image_to_pdf_btn.setMinimumHeight(40)

        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(subtitle)
        layout.addSpacing(30)
        layout.addWidget(self.merge_pdf_btn)
        layout.addWidget(self.image_to_pdf_btn)

        self.setLayout(layout)


class MergerApp(QMainWindow):
    """Main window with operation registry and welcome screen."""

    def __init__(self):
        super().__init__()

        self._labels = Labels()
        self._layout_config = LayoutConfig()

        self._view_aggregator = ViewAggregator(
            self._labels,
            pdf_merger_service=PdfMergerService(),
            image_merger_service=ImageMergerService()
        )

        self._operations = []
        self._setup_ui()

    # -------------------------
    # UI Setup
    # -------------------------

    def _setup_ui(self):

        self.setWindowTitle(self._labels.APP_NAME)

        self.setGeometry(
            self._layout_config.WINDOW_X_POS,
            self._layout_config.WINDOW_Y_POS,
            self._layout_config.WINDOW_WIDTH,
            self._layout_config.WINDOW_HEIGHT
        )

        self._create_menu_bar()

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

        self.stacked = QStackedWidget()
        layout.addWidget(self.stacked)

        # Welcome screen
        self.welcome_view = WelcomeView()
        self.welcome_index = self.stacked.addWidget(self.welcome_view)

        # Register operations
        self._register_operations()

        # Show welcome screen first
        self.stacked.setCurrentIndex(self.welcome_index)

    # -------------------------
    # Menu Bar
    # -------------------------

    def _create_menu_bar(self):

        menu_bar = self.menuBar()

        # File
        file_menu = menu_bar.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

        # Operations
        self.operations_menu = menu_bar.addMenu("Operations")

        # Help
        help_menu = menu_bar.addMenu("Help")

        how_to_action = QAction("How to use", self)
        how_to_action.triggered.connect(self._show_help)

        about_action = QAction("About", self)
        about_action.triggered.connect(self._show_about)

        help_menu.addAction(how_to_action)
        help_menu.addAction(about_action)

    # -------------------------
    # Operation Registration
    # -------------------------

    def _register_operations(self):

        self._register_operation(
            "Merge PDFs",
            self._view_aggregator.pdf_collection_merge_view.get_widget()
        )

        self._register_operation(
            "Images → PDF",
            self._view_aggregator.image_to_pdf_merge_view.get_widget()
        )

    def _register_operation(self, name: str, widget: QWidget):

        index = self.stacked.addWidget(widget)

        action = QAction(name, self)
        action.triggered.connect(lambda _, i=index: self._switch_operation(i))

        self.operations_menu.addAction(action)

        self._operations.append({
            "name": name,
            "widget": widget,
            "index": index
        })

        # Connect welcome screen buttons
        if name == "Merge PDFs":
            self.welcome_view.merge_pdf_btn.clicked.connect(
                lambda: self._switch_operation(index)
            )

        if name == "Images → PDF":
            self.welcome_view.image_to_pdf_btn.clicked.connect(
                lambda: self._switch_operation(index)
            )

    # -------------------------
    # Navigation
    # -------------------------

    def _switch_operation(self, index: int):
        self.stacked.setCurrentIndex(index)

    # -------------------------
    # Help Dialogs
    # -------------------------

    def _show_help(self):
        QMessageBox.information(
            self,
            "How to Use",
            "1. Choose an operation.\n"
            "2. Drag and drop files.\n"
            "3. Select where to save.\n"
            "4. Click Merge."
        )

    def _show_about(self):
        QMessageBox.information(
            self,
            "About",
            f"{self._labels.APP_NAME}\n\n"
            "A simple desktop utility for merging PDFs and images."
        )


def main():
    app = QApplication(sys.argv)
    ThemeProvider.apply_theme(app, "light")
    window = MergerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
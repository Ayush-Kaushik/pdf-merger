# Author: Ayush Kaushik

import sys
from PyQt5.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QWidget, 
    QPushButton, 
    QVBoxLayout,
    QHBoxLayout, 
    QStackedWidget
)

from PyQt5.QtCore import Qt

from pdf_merger.src.services.image_merger_service import ImageMergerService
from pdf_merger.src.services.pdf_merger_service import PdfMergerService

from pdf_merger.src.ui.themes.theme_provider import ThemeProvider
from pdf_merger.src.ui.view_aggregator import ViewAggregator
from pdf_merger.src.ui.constants import Labels, LayoutConfig

# Keep track of active mode
MODE_PDF_MERGE = 0
MODE_IMAGE_TO_PDF = 1

class MergerApp(QMainWindow):
    """Main window for the PDF Merger application using button-based tabs."""
    def __init__(self):
        super().__init__()
        self._labels = Labels()
        self._layout_config = LayoutConfig()
        self._view_aggregator = ViewAggregator(
            self._labels, 
            pdf_merger_service=PdfMergerService(), 
            image_merger_service=ImageMergerService())

        self.active_mode_index = MODE_PDF_MERGE
        self._setup_ui()

    def _setup_ui(self):
        """Sets up the main window UI."""
        self.setWindowTitle(self._labels.APP_NAME)
        self.setGeometry(
            self._layout_config.WINDOW_X_POS,
            self._layout_config.WINDOW_Y_POS,
            self._layout_config.WINDOW_WIDTH,
            self._layout_config.WINDOW_HEIGHT
        )

        # Main container widget
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Mode Buttons (like web tabs)
        self.mode_buttons_layout = QHBoxLayout()
        self.merge_pdf_btn = QPushButton(self._labels.MERGE_PDF_TAB_TITLE)
        self.image_to_pdf_btn = QPushButton(self._labels.IMAGE_TO_PDF_TAB_TITLE)

        self._setup_mode_button(self.merge_pdf_btn, index=MODE_PDF_MERGE)
        self._setup_mode_button(self.image_to_pdf_btn, index=MODE_IMAGE_TO_PDF)

        self.mode_buttons_layout.addWidget(self.merge_pdf_btn)
        self.mode_buttons_layout.addWidget(self.image_to_pdf_btn)
        main_layout.addLayout(self.mode_buttons_layout)

        # Stacked widget for pages
        self.stacked = QStackedWidget()
        self.stacked.addWidget(self._view_aggregator.image_to_pdf_merge_view.get_widget())
        self.stacked.addWidget(self._view_aggregator.pdf_collection_merge_view.get_widget())
        main_layout.addWidget(self.stacked)

        # Set default active
        self._update_mode_buttons()

    def _setup_mode_button(self, button: QPushButton, index: int):
        """Style a mode button and connect click to stacked widget."""
        button.setCheckable(True)
        button.setCursor(Qt.PointingHandCursor)
        button.setMinimumHeight(50)
        button.clicked.connect(lambda checked, i=index: self._switch_mode(i))

    def _switch_mode(self, index: int):
        """Switch stacked widget page and update button styles."""
        if index == self.active_mode_index:
            return
        
        self.active_mode_index = index
        self.stacked.setCurrentIndex(index)
        self._update_mode_buttons()

    def _update_mode_buttons(self):
        """Update the styles of the buttons based on active mode."""
        self.merge_pdf_btn.setChecked(self.active_mode_index == 0)
        self.image_to_pdf_btn.setChecked(self.active_mode_index == 1)

        self.merge_pdf_btn.setProperty("active", self.active_mode_index == 0)
        self.image_to_pdf_btn.setProperty("active", self.active_mode_index == 1)

        # Force re-polish so QSS reacts to property change 
        # TODO: Note expensive operation, optimize it
        for btn in [self.merge_pdf_btn, self.image_to_pdf_btn]:
            btn.style().unpolish(btn)
            btn.style().polish(btn)
            btn.update()

def main():
    app = QApplication(sys.argv)
    ThemeProvider.apply_theme(app, "light")
    window = MergerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
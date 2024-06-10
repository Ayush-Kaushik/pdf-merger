import sys

import img2pdf
from PyPDF2 import PdfFileMerger
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QMainWindow, QTabWidget, QApplication

from pdf_merger.src.services import ImageService, PDFService
from pdf_merger.src.views import AppLayoutConfig, ViewAggregator
from pdf_merger.src.views.labels import Labels


class MergerApp(QMainWindow):
    def __init__(self, aggregator: ViewAggregator, config: AppLayoutConfig):
        super().__init__()
        self.config = config
        self.viewAggregator = aggregator
        self.initialize()

    def initialize(self):
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.setWindowTitle(self.config.title)
        self.setGeometry(self.config.left, self.config.top, self.config.width, self.config.height)

        '''
        Append tabs for each service
            - PDF Service
            - Image Service
        '''
        self.tabs = QTabWidget()
        self.tabs.addTab(self.viewAggregator.imageToPDFMergeView.get_widget(), Labels.IMAGE_TO_PDF_TAB_TITLE)
        self.tabs.addTab(self.viewAggregator.pdfCollectionMergeView.get_widget(), Labels.MERGE_PDF_TAB_TITLE)

        self.tabsLayout = QHBoxLayout()
        self.tabsLayout.addWidget(self.tabs)
        self.widget.setLayout(self.tabsLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # setting up dependencies to be injected
    viewAggregator = ViewAggregator(
        PDFService(PdfFileMerger(), [], ""),
        ImageService(img2pdf, [], ""),
        AppLayoutConfig("Image Merger", 10, 10, 500, 400),
        AppLayoutConfig("PDF Merger", 10, 10, 500, 400),

        Labels()
    )

    appConfig = AppLayoutConfig("PDF Merger", 10, 10, 500, 400)

    ex = MergerApp(viewAggregator, appConfig)
    sys.exit(app.exec_())
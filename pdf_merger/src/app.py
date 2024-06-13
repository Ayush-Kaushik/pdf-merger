# Author: Ayush Kaushik

import sys

import injector
from injector import Injector, inject, Module, Binder
import img2pdf
from PyPDF2 import PdfFileMerger
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QMainWindow, QTabWidget, QApplication

from pdf_merger.src.services import ImageMergerService, PdfMergerService
from pdf_merger.src.views import AppLayoutConfig, ViewAggregator
from pdf_merger.src.views.labels import Labels


class AppConfigModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(AppLayoutConfig, to=AppLayoutConfig("PDF Merger", 10, 10, 500, 400), scope=injector.singleton)


class ViewAggregatorContainerModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(PdfMergerService, to=PdfMergerService(PdfFileMerger(), [], ""), scope=injector.singleton)
        binder.bind(ImageMergerService, to=ImageMergerService(img2pdf, [], ""), scope=injector.singleton)
        binder.bind(Labels, to=Labels())
        binder.bind(ViewAggregator, to=ViewAggregator, scope=injector.singleton)


class MergerApp(QMainWindow):
    @inject
    def __init__(self, aggregator: ViewAggregator, config: AppLayoutConfig):
        super().__init__()
        self.widget = None
        self.tabs = None
        self.tabsLayout = None
        
        self.config = config
        self.viewAggregator = aggregator
        self.initialize()

    def initialize(self):
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.setWindowTitle(self.config.title)
        self.setGeometry(self.config.left, self.config.top, self.config.width, self.config.height)

        self.tabs = QTabWidget()
        self.tabs.addTab(self.viewAggregator.imageToPDFMergeView.get_widget(), Labels.IMAGE_TO_PDF_TAB_TITLE)
        self.tabs.addTab(self.viewAggregator.pdfCollectionMergeView.get_widget(), Labels.MERGE_PDF_TAB_TITLE)

        self.tabsLayout = QHBoxLayout()
        self.tabsLayout.addWidget(self.tabs)
        self.widget.setLayout(self.tabsLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    injector_instance = Injector([AppConfigModule, ViewAggregatorContainerModule])
    ex = injector_instance.get(MergerApp)
    sys.exit(app.exec_())

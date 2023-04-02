import sys
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QMainWindow, QTabWidget, QApplication
from views import AppLayoutConfig, ViewAggregator, Labels

class MergerApp(QMainWindow):
    def __init__(self, viewAggregtor: ViewAggregator, config: AppLayoutConfig):
        super().__init__()
        self.config = config
        self.viewAggregtor = viewAggregtor
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.initializeAppUI()
        self.widget.setLayout(QHBoxLayout())

    def initializeAppUI(self):
        self.setWindowTitle(self.config.title)
        self.setGeometry(self.config.left, self.config.top,
                         self.config.width, self.config.height)

        '''
        Append tabs for each service
            - PDF Service
            - Image Service
        '''
        self.tabs = QTabWidget()
        self.tabs.addTab(self.viewAggregtor.imageToPDFMergeView.getTab(
        ), Labels.IMAGE_TO_PDF_TAB_TITLE)
        self.tabs.addTab(self.viewAggregtor.pdfCollectionMergeView.getTab(
        ), Labels.MERGE_PDF_TAB_TITLE)

        self.tabsLayout = QHBoxLayout()
        self.tabsLayout.addWidget(self.tabs)
        self.widget.setLayout(self.tabsLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    viewAggregtor = ViewAggregator()
    appConfig = AppLayoutConfig("File Merger", 10, 10, 500, 400)

    ex = MergerApp(viewAggregtor, appConfig)
    sys.exit(app.exec_())

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from src.views.Labels import Labels

from src.views.ViewAggregator import ViewAggregator
from src.config.AppLayoutConfig import AppLayoutConfig

class MergerApp(QMainWindow):
    def __init__(self, viewAggregtor: ViewAggregator, config: AppLayoutConfig, labels: Labels):
        super().__init__()
        self.config = config 
        self.labels = labels
        self.viewAggregtor = viewAggregtor        
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.initializeAppUI()
        self.widget.setLayout(QHBoxLayout())
        
    def initializeAppUI(self):
        self.setWindowTitle(self.config.title)
        self.setGeometry(self.config.left, self.config.top, self.config.width, self.config.height)
        
        '''
        Append tabs for each service
            - PDF Service
            - Image Service
        '''
        self.tabs = QTabWidget()
        self.tabs.addTab(self.viewAggregtor.imageToPDFMergeView.getTab(), "Convert Image into PDF")
        self.tabs.addTab(self.viewAggregtor.pdfCollectionMergeView.getTab(), "Merge PDF")
        
        self.tabsLayout = QHBoxLayout()
        self.tabsLayout.addWidget(self.tabs)
        self.widget.setLayout(self.tabsLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    viewAggregtor = ViewAggregator()
    appConfig = AppLayoutConfig("File Merger", 10, 10, 500, 400)
    labels = Labels()
    
    ex = MergerApp(viewAggregtor, appConfig, labels)
    sys.exit(app.exec_())

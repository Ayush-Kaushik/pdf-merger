from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import img2pdf

from src.services.ImageService import ImageService
from src.views.ButtonFactory import ButtonFactory
from src.config.AppLayoutConfig import AppLayoutConfig
from src.views.DragAndDropArea import DragAndDropArea
from src.views.Labels import Labels


class ImageToPDFMergeView():
    '''
        Includes the complete view for Merging Images into PDF
    '''
    
    def __init__(self):
        self.tab = QWidget()
        self.imageService = ImageService(img2pdf, [], "")
        self.config = AppLayoutConfig("Image Merger", 10, 10, 500, 400)
        self.labels = Labels()
        self.initializeLayout()
    
    def getOutputFilePath(self) -> str:
        directory = QFileDialog.getExistingDirectory(
            None, self.labels.CHOOSE_DIRECTORY, "")
        savedLocation = ""
        if directory != "":
            savedLocation = directory + "/merged.pdf"        
            self.imageService.setTargetFilePath(savedLocation)
        self.textbox.setText(savedLocation)

    def resetView(self):
        self.imageService.setTargetFilePath("")
        self.textbox.setText(self.imageService.targetFilePath)
        self.imageService.clearQueue()
        self.dragAndDropView.clearQueue()
        
    # return location of merged pdf if successful
    # otherwise return null
    def mergeMedia(self):
        try:
            self.imageService.mergeQueue()
        except Exception as exception:
            print(exception)
        finally:
            self.resetView()
        
    def initializeLayout(self):
        self.tab.layout = QVBoxLayout()
        
        # Input box that shows location of merged file
        self.textbox = QLineEdit()
        self.textbox.resize((self.config.width - 200), 40)
        
        # Button to open dialog to select location to place merged file
        self.saveButton = ButtonFactory.create_button(self, "Save To", self.getOutputFilePath)
        self.deleteButton = ButtonFactory.create_button(self, "Reset", self.resetView)
        self.mergeButton = ButtonFactory.create_button(self, "Merge", self.mergeMedia)
        
        # PDF drag and drop area
        self.dragAndDropView = DragAndDropArea(self.imageService)

        # Setup their layouts
        self.verticalLayout = QVBoxLayout()

        self.horizontalBoyLayout = QHBoxLayout()
        self.horizontalBoyLayout.addWidget(self.textbox, 2)
        self.horizontalBoyLayout.addWidget(self.saveButton, 0)
        
        self.dragAndDropAreaLayout = QHBoxLayout()
        self.dragAndDropAreaLayout.addWidget(self.dragAndDropView)

        self.callToActionLayout = QHBoxLayout()
        self.callToActionLayout.addWidget(self.deleteButton, 1)
        self.callToActionLayout.addWidget(self.mergeButton, 1)

        self.verticalLayout.addLayout(self.horizontalBoyLayout)
        self.verticalLayout.addLayout(self.dragAndDropAreaLayout)
        self.verticalLayout.addLayout(self.callToActionLayout)
        self.tab.setLayout(self.verticalLayout)
    
        
    def getTab(self):
        return self.tab
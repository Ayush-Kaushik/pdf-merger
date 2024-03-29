# Author: Ayush Kaushik

from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QLineEdit, QHBoxLayout, QLabel
import img2pdf

from ..services import ImageService
from .button_factory import ButtonFactory
from .app_layout_config import AppLayoutConfig
from .drag_drop_area import DragAndDropArea
from .labels import Labels
from .popup_factory import PopupFactory

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
            popup = PopupFactory.getPopup(
                    "Info", "Task Successful!")
            popup.exec_()
        except Exception as exception:
            print(exception)
        finally:
            self.resetView()
        
    def initializeLayout(self):
        self.tab.layout = QVBoxLayout()
        
        # Input box that shows location of merged file
        self.textbox = QLineEdit()
        self.textbox.resize((self.config.width - 200), 40)
        self.textbox.setReadOnly(True)
        
        # Button to open dialog to select location to place merged file
        self.saveButton = ButtonFactory.create_button(self, "Save To", self.getOutputFilePath)
        self.deleteButton = ButtonFactory.create_button(self, "Reset Files", self.resetView)
        self.mergeButton = ButtonFactory.create_button(self, "Merge Files", self.mergeMedia)
        
        # PDF drag and drop area
        self.dragAndDropView = DragAndDropArea(self.imageService)

        # Setup their layouts
        self.verticalLayout = QVBoxLayout()

        self.horizontalBoyLayout = QHBoxLayout()
        self.horizontalBoyLayout.addWidget(self.textbox, 2)
        self.horizontalBoyLayout.addWidget(self.saveButton, 0)
        
        self.dragAndDropAreaLayout = QVBoxLayout()
        self.dragAndDropAreaLayout.addWidget(QLabel("Drag and drop files below"))
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
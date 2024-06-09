# Author: Ayush Kaushik

from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QLineEdit, QHBoxLayout, QLabel
import img2pdf

from pdf_merger.src.services.image_service import ImageService
from pdf_merger.src.views import ButtonFactory, AppLayoutConfig, DragAndDropArea
from pdf_merger.src.views.labels import Labels
from pdf_merger.src.views.popup_factory import PopupFactory

'''
    Complete view for merging multiple images into single PDF
'''


class ImageToPDFMergeView:
    def __init__(self):
        self.tab = QWidget()
        self.imageService = ImageService(img2pdf, [], "")
        self.config = AppLayoutConfig("Image Merger", 10, 10, 500, 400)
        self.labels = Labels()
        self.initializeLayout()

    def getOutputFilePath(self):
        directory = QFileDialog.getExistingDirectory(
            None, self.labels.CHOOSE_DIRECTORY, "")
        save_file_path = ""
        if directory != "":
            save_file_path = directory + "/merged.pdf"
            self.imageService.set_output_target(save_file_path)
        self.textbox.setText(save_file_path)

    def resetView(self):
        self.imageService.set_output_target("")
        self.textbox.setText(self.imageService.target_file_path)
        self.imageService.clear_list()
        self.dragAndDropView.clearQueue()

    # return location of merged pdf if successful
    # otherwise return null
    def mergeMedia(self):
        try:
            self.imageService.merge_files()
            popup = PopupFactory.getPopup("Info", "Task Successful!")
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
        self.saveButton = ButtonFactory.create(self, "Save To", self.getOutputFilePath)
        self.deleteButton = ButtonFactory.create(self, "Reset Files", self.resetView)
        self.mergeButton = ButtonFactory.create(self, "Merge Files", self.mergeMedia)

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

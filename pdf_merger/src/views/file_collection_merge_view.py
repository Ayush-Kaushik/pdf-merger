# Author: Ayush Kaushik

from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QLineEdit, QHBoxLayout, QLabel

from pdf_merger.src.views.app_layout_config import AppLayoutConfig
from pdf_merger.src.views.button_factory import ButtonFactory
from pdf_merger.src.views.drag_drop_area import DragAndDropArea
from pdf_merger.src.views.labels import Labels
from pdf_merger.src.views.popup_factory import PopupFactory

from pdf_merger.src.services.abstract_merger_service import AbstractFileMergerService

'''
    Includes the complete view for Merging files into single PDF
'''


class FileCollectionMergeView(QWidget):
    def __init__(
            self,
            service: AbstractFileMergerService,
            config: AppLayoutConfig,
            labels: Labels
    ):
        super().__init__()
        self.fileMergerService = service
        self.config = config
        self.labels = labels
        self.initialize_layout()
    
    def get_output_file_path(self):
        directory = QFileDialog.getExistingDirectory(None, self.labels.CHOOSE_DIRECTORY, "")
        saved_file_path = ""
        if directory != "":
            saved_file_path = directory + "/merged.pdf"
            self.fileMergerService.set_output_target(saved_file_path)
        self.textbox.setText(saved_file_path)
        
    def reset_widget(self):
        self.fileMergerService.set_output_target("")
        self.textbox.setText(self.fileMergerService.target_file_path)
        self.fileMergerService.clear_list()
        self.dragAndDropView.clear_area()

    def merge_files(self):
        try:
            self.fileMergerService.merge_files()
            popup = PopupFactory.get("Info", "Task Successful!")
            popup.exec_()
        except Exception as exception:
            print(exception)
        finally:
            self.reset_widget()
        
    def initialize_layout(self):
        self.layout = QVBoxLayout()
        
        # Input box that shows location of merged file
        self.textbox = QLineEdit()
        self.textbox.resize((self.config.width - 200), 40)
        self.textbox.setReadOnly(True)
        
        # Button to open dialog to select location to place merged file
        self.saveButton = ButtonFactory.create("Save To", self.get_output_file_path)
        self.deleteButton = ButtonFactory.create("Reset Files", self.reset_widget)
        self.mergeButton = ButtonFactory.create("Merge Files", self.merge_files)
        
        # PDF drag and drop area
        self.dragAndDropView = DragAndDropArea(self.fileMergerService)

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
        
        self.setLayout(self.verticalLayout)
        
    def get_widget(self):
        return self

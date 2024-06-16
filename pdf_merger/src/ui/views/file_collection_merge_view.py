# Author: Ayush Kaushik

from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QLineEdit, QHBoxLayout, QLabel

from pdf_merger.src.ui.components.app_layout_config import AppLayoutConfig
from pdf_merger.src.ui.components.button_factory import ButtonFactory
from pdf_merger.src.ui.components.drag_drop_area import DragAndDropArea
from pdf_merger.src.ui.constants import LabelsConstants
from pdf_merger.src.ui.components.popup_factory import PopupFactory

from pdf_merger.src.services.abstract_file_merger_service import AbstractFileMergerService

'''
    Includes the complete view for Merging files into single PDF
'''


class FileCollectionMergeView(QWidget):
    def __init__(
            self,
            service: AbstractFileMergerService,
            config: AppLayoutConfig,
            labels: LabelsConstants
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
        # Input box that shows location of merged file
        text_box = QLineEdit()
        text_box.resize((self.config.width - 200), 40)
        
        # Button to open dialog to select location to place merged file
        save_button = ButtonFactory.create(self.labels.SAVE_TO, self.get_output_file_path)
        delete_button = ButtonFactory.create(self.labels.RESET, self.reset_widget)
        merge_button = ButtonFactory.create(self.labels.MERGE, self.merge_files)
        
        # PDF drag and drop area
        drag_drop_view = DragAndDropArea(self.fileMergerService)

        # Setup their layouts
        horizontal_box_layout = QHBoxLayout()
        horizontal_box_layout.addWidget(text_box, 2)
        horizontal_box_layout.addWidget(save_button, 0)
        
        drag_drop_area_layout = QVBoxLayout()
        drag_drop_area_layout.addWidget(QLabel(self.labels.DRAG_AND_DROP_FILES))
        drag_drop_area_layout.addWidget(drag_drop_view)

        call_to_action_layout = QHBoxLayout()
        call_to_action_layout.addWidget(delete_button, 1)
        call_to_action_layout.addWidget(merge_button, 1)

        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(horizontal_box_layout)
        vertical_layout.addLayout(drag_drop_area_layout)
        vertical_layout.addLayout(call_to_action_layout)

        self.setLayout(vertical_layout)
        
    def get_widget(self):
        return self

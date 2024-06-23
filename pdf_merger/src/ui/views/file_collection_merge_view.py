# Author: Ayush Kaushik

from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QLineEdit, QHBoxLayout, QLabel

from pathlib import Path
from pdf_merger.src.ui.components.app_layout_config import AppLayoutConfig
from pdf_merger.src.ui.components.button_factory import ButtonFactory
from pdf_merger.src.ui.components.drag_drop_area import DragAndDropArea
from pdf_merger.src.ui.constants import LabelsConstants
from pdf_merger.src.ui.components.popup_factory import PopupFactory, PopupType

from pdf_merger.src.services.abstract_file_merger_service import AbstractFileMergerService

'''
    Includes the complete view for Merging files into single PDF.
'''


class FileCollectionMergeView(QWidget):
    def __init__(
            self,
            service: AbstractFileMergerService,
            config: AppLayoutConfig,
            labels: LabelsConstants
    ):
        super().__init__()
        self.drag_drop_view = None
        self.merge_button = None
        self.delete_button = None
        self.save_button = None
        self.text_box = None
        self.fileMergerService = service
        self.config = config
        self.labels = labels
        self.initialize_layout()

    def get_output_file_path(self):
        save_file_path: Path = Path()
        directory = QFileDialog.getExistingDirectory(None, self.labels.CHOOSE_DIRECTORY, "")

        if directory != "":
            save_file_path = directory + "/merged.pdf"
            self.fileMergerService.set_output_target(Path(save_file_path))
        self.text_box.setText(save_file_path)
        
    def reset_widget(self):
        self.fileMergerService.set_output_target(Path())
        self.text_box.setText(str(self.fileMergerService.target_file_path))
        self.fileMergerService.clear_list()
        self.drag_drop_view.clear_area()

    def merge_files(self):
        if self.fileMergerService.merge_files():
            popup = PopupFactory.get(PopupType.INFO, "Task Successful!")
            popup.exec_()
            self.reset_widget()
        else:
            popup = PopupFactory.get(PopupType.ERROR, "Task Failed!")
            popup.exec_()

    def initialize_layout(self):
        # Input box that shows location of merged file
        self.text_box = QLineEdit()
        self.text_box.resize((self.config.width - 200), 40)
        
        # Button to open dialog to select location to place merged file
        self.save_button = ButtonFactory.create(self.labels.SAVE_TO, self.get_output_file_path)
        self.delete_button = ButtonFactory.create(self.labels.RESET, self.reset_widget)
        self.merge_button = ButtonFactory.create(self.labels.MERGE, self.merge_files)
        
        # PDF drag and drop area
        self.drag_drop_view = DragAndDropArea(self.fileMergerService)

        # Setup their layouts
        horizontal_box_layout = QHBoxLayout()
        horizontal_box_layout.addWidget(self.text_box, 2)
        horizontal_box_layout.addWidget(self.save_button, 0)
        
        drag_drop_area_layout = QVBoxLayout()
        drag_drop_area_layout.addWidget(QLabel(self.labels.DRAG_AND_DROP_FILES))
        drag_drop_area_layout.addWidget(self.drag_drop_view)

        call_to_action_layout = QHBoxLayout()
        call_to_action_layout.addWidget(self.delete_button, 1)
        call_to_action_layout.addWidget(self.merge_button, 1)

        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(horizontal_box_layout)
        vertical_layout.addLayout(drag_drop_area_layout)
        vertical_layout.addLayout(call_to_action_layout)

        self.setLayout(vertical_layout)
        
    def get_widget(self):
        return self

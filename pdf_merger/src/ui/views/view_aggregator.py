# Author: Ayush Kaushik

from pdf_merger.src.ui.constants import LabelsConstants
from pdf_merger.src.ui.components.app_layout_config import AppLayoutConfig
from pdf_merger.src.ui.views.file_collection_merge_view import FileCollectionMergeView
from pdf_merger.src.services.image_merger_service import ImageMergerService
from pdf_merger.src.services.pdf_merger_service import PdfMergerService
from injector import inject

'''
    Collects all the ui to be passed into the main application
'''


class ViewAggregator:
    @inject
    def __init__(
            self,
            pdf_service: PdfMergerService,
            image_service: ImageMergerService,
            widget_layout_config: AppLayoutConfig,
            labels: LabelsConstants
    ):
        self.imageToPDFMergeView = FileCollectionMergeView(pdf_service, widget_layout_config, labels)
        self.pdfCollectionMergeView = FileCollectionMergeView(image_service, widget_layout_config, labels)

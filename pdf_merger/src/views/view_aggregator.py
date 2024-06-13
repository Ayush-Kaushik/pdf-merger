# Author: Ayush Kaushik

from pdf_merger.src.views import AppLayoutConfig, Labels
from pdf_merger.src.views.file_collection_merge_view import FileCollectionMergeView
from pdf_merger.src.services.image_merger_service import ImageMergerService
from pdf_merger.src.services.pdf_merger_service import PdfMergerService
from injector import inject

'''
    Collects all the views to be passed into the main application
'''


class ViewAggregator:
    @inject
    def __init__(
            self,
            pdf_service: PdfMergerService,
            image_service: ImageMergerService,
            widget_layout_config: AppLayoutConfig,
            labels: Labels
    ):
        self.imageToPDFMergeView = FileCollectionMergeView(pdf_service, widget_layout_config, labels)
        self.pdfCollectionMergeView = FileCollectionMergeView(image_service, widget_layout_config, labels)

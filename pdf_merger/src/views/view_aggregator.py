# Author: Ayush Kaushik
from pdf_merger.src.views import AppLayoutConfig, Labels
from pdf_merger.src.views.file_collection_merge_view import FileCollectionMergeView
from pdf_merger.src.services.image_service import ImageService
from pdf_merger.src.services.pdf_service import PDFService

'''
    Collects all the views to be passed into the main application
'''


class ViewAggregator:
    def __init__(
            self,
            pdf_service: PDFService,
            image_service: ImageService,
            pdf_widget_layout_config: AppLayoutConfig,
            image_widget_layout_config: AppLayoutConfig,
            labels: Labels
    ):
        self.imageToPDFMergeView = FileCollectionMergeView(pdf_service, pdf_widget_layout_config, labels)
        self.pdfCollectionMergeView = FileCollectionMergeView(image_service, image_widget_layout_config, labels)

# Author: Ayush Kaushik

from pdf_merger.src.ui.constants import Labels, LayoutConfig
from pdf_merger.src.ui.file_collection_merge_view import FileCollectionMergeView

from pdf_merger.src.services.image_merger_service import ImageMergerService
from pdf_merger.src.services.pdf_merger_service import PdfMergerService

class ViewAggregator:
    """Container for UI components to be passed into the main application."""

    def __init__(self, 
                 labels: Labels = None,
                 image_merger_service: ImageMergerService = None, 
                 pdf_merger_service: PdfMergerService = None):
        self._labels = labels
        self._image_merger_service = image_merger_service
        self._pdf_merger_service = pdf_merger_service

        self.image_to_pdf_merge_view = FileCollectionMergeView(
            self._image_merger_service, 
            self._labels
        )
        
        self.pdf_collection_merge_view = FileCollectionMergeView(
            self._pdf_merger_service, 
            self._labels
        )
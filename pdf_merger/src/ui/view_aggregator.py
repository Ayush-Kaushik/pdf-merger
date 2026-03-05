# Author: Ayush Kaushik

from pdf_merger.src.ui.constants import Labels, LayoutConfig
from pdf_merger.src.ui.file_collection_merge_view import FileCollectionMergeView

from pdf_merger.src.services.image_merger_service import ImageMergerService
from pdf_merger.src.services.pdf_merger_service import PdfMergerService

class ViewAggregator:
    """Container for UI components to be passed into the main application."""

    def __init__(self, layout_config: LayoutConfig = None, labels: Labels = None,
                 image_merger_service: ImageMergerService = None, pdf_merger_service: PdfMergerService = None):
        
        self._layout_config = layout_config or LayoutConfig()
        self._labels = labels or Labels()
        self._image_merger_service = image_merger_service or ImageMergerService()
        self._pdf_merger_service = pdf_merger_service or PdfMergerService()

        self.image_to_pdf_merge_view = FileCollectionMergeView(
            self._image_merger_service, 
            self._layout_config, 
            self._labels
        )
        
        self.pdf_collection_merge_view = FileCollectionMergeView(
            self._pdf_merger_service, 
            self._layout_config, 
            self._labels
        )
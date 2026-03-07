# Author: Ayush Kaushik

from dataclasses import dataclass

@dataclass(frozen=True)
class LayoutConfig:
    """Configuration for the layout of the application."""
    WINDOW_WIDTH: int       = 800
    WINDOW_HEIGHT: int      = 600
    WINDOW_X_POS: int       = 100
    WINDOW_Y_POS: int       = 100
    BUTTON_WIDTH: int       = 80
    BUTTON_HEIGHT: int      = 30
    MARGIN: int             = 10

@dataclass(frozen=True)
class Labels:
    """Labels used in the application."""
    APP_NAME: str               = "PDF Merger"
    IMAGE_TO_PDF_TAB_TITLE: str = "Merge Images to PDF"
    MERGE_PDF_TAB_TITLE: str    = "Merge PDFs to PDF"
    CHOOSE_DIRECTORY: str       = "Choose Directory"
    DRAG_AND_DROP_FILES: str    = "Drag and drop files below"
    SAVE_TO: str                = "Select Save Location"
    RESET: str                  = "Clear All"
    MERGE: str                  = "Merge Files"
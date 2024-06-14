# Author: Ayush Kaushik

from pdf_merger.src.ui.constants import LabelsConstants, UILayoutConstants


class AppLayoutConfig:
    def __init__(self,
                 title: str = LabelsConstants.APP_NAME,
                 left: int = UILayoutConstants.MARGIN,
                 top: int = UILayoutConstants.MARGIN,
                 height: int = UILayoutConstants.WINDOW_HEIGHT,
                 width: int = UILayoutConstants.WINDOW_WIDTH):
        self.title = title
        self.left = left
        self.top = top
        self.width = width
        self.height = height

# Author: Ayush Kaushik

from .labels import Labels
from .ui_layout_constants import UILayoutConstants

class AppLayoutConfig:
    def __init__(self, title: str=Labels.APP_NAME, left: int=UILayoutConstants.MARGIN, top: int=UILayoutConstants.MARGIN, height: int=UILayoutConstants.WINDOW_HEIGHT, width :int=UILayoutConstants.WINDOW_WIDTH):
        self.title = title
        self.left = left
        self.top = top
        self.width = width
        self.height = height

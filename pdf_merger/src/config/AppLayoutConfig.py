# Author: Ayush Kaushik
from views.labels import APP_NAME
from views.ui_layout_constants import UILayoutConstants


class AppLayoutConfig:
    def __init__(self, title=APP_NAME: str, left=UILayoutConstants.MARGIN: int, top=UILayoutConstants.MARGIN: int, height=UILayoutConstants.WINDOW_HEIGHT: int, width=UILayoutConstants.WINDOW_WIDTH: int):
        self.title = title
        self.left = left
        self.top = top
        self.width = width
        self.height = height

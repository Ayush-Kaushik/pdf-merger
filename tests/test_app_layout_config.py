# Author: Ayush Kaushik

import unittest
from pdf_merger.src.ui.components import AppLayoutConfig
from pdf_merger.src.ui.constants import LabelsConstants


class TestAppLayoutConfig(unittest.TestCase):
    def test_constructor_defaults(self):
        config = AppLayoutConfig()
        self.assertEqual(config.title, LabelsConstants.APP_NAME)
        self.assertEqual(config.left, 10)
        self.assertEqual(config.top, 10)
        self.assertEqual(config.width, 800)
        self.assertEqual(config.height, 600)

    def test_constructor_custom_values(self):
        title = "My App"
        left = 20
        top = 20
        height = 700
        width = 900
        config = AppLayoutConfig(title=title, left=left, top=top, height=height, width=width)
        self.assertEqual(config.title, title)
        self.assertEqual(config.left, left)
        self.assertEqual(config.top, top)
        self.assertEqual(config.width, width)
        self.assertEqual(config.height, height)


if __name__ == '__main__':
    unittest.main()

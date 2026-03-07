import os
from PyQt5.QtWidgets import QApplication

class ThemeProvider:
    THEME_DIR = os.path.join(os.path.dirname(__file__))

    @staticmethod
    def load_qss_file(filename: str) -> str:
        path = os.path.join(ThemeProvider.THEME_DIR, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"QSS file not found: {path}")
        with open(path, "r") as f:
            return f.read()

    @staticmethod
    def get_theme(theme_name: str) -> str:
        """Return QSS string based on theme name."""
        theme_name = theme_name.lower()
        if theme_name == "dark":
            return ThemeProvider.load_qss_file("dark_theme.qss")
        elif theme_name == "light":
            return ThemeProvider.load_qss_file("light_theme.qss")
        else:
            raise ValueError(f"Unknown theme: {theme_name}")
        
    @staticmethod
    def apply_theme(app: QApplication, theme_name: str):
        """Apply the selected theme to the application."""
        qss = ThemeProvider.get_theme(theme_name)
        print(qss)
        app.setStyleSheet(qss)
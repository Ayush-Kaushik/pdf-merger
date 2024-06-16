# Author: Ayush Kaushik

from abc import abstractmethod, ABC

import pathlib
from typing import Dict, List


class AbstractFileMergerService(ABC):
    def __init__(
            self,
            allowed_extensions: Dict[str, str],
            file_list: List[pathlib.Path],
            target_file_path: pathlib.Path
    ):
        self.allowed_file_extensions = allowed_extensions
        self.target_file_path = target_file_path
        self.file_list = file_list

    @abstractmethod
    def merge_files(self):
        """
        Merges the files in the file list into a single file.
        """
        pass

    def clear_list(self):
        """
        Clears the file list.
        """
        self.file_list: list[pathlib.Path] = []

    def append_file(self, file_path: pathlib.Path):
        """
        Appends a file to the file list.
        """
        self.file_list.append(file_path)

    def set_output_target(self, file_path: pathlib.Path):
        """
        Sets the output target file path.
        """
        self.target_file_path = file_path

    def get_output_target(self):
        """
        Returns the output target file path.
        """
        return self.target_file_path

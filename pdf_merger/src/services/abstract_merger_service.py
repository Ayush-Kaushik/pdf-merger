# Author: Ayush Kaushik

from abc import abstractmethod, ABC

import pathlib


class AbstractFileMergerService(ABC):
    def __init__(self, allowed_extensions, target_file_path: pathlib.Path):
        self.allowed_file_extensions = allowed_extensions
        self.target_file_path = target_file_path

    @abstractmethod
    def merge_files(self):
        pass

    @abstractmethod
    def clear_list(self):
        pass

    @abstractmethod
    def append_file(self, file_path):
        pass

    @abstractmethod
    def set_output_target(self, file_path):
        pass

    @abstractmethod
    def get_output_target(self):
        pass

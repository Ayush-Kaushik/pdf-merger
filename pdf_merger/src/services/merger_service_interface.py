# Author: Ayush Kaushik

from abc import abstractmethod


class FileMergerServiceInterface:
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


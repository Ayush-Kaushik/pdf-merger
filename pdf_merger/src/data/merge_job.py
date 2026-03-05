from pathlib import Path
from dataclasses import dataclass, field
from typing import List

@dataclass
class MergeJob:
    files: List[Path] = field(default_factory=list)
    output_file: Path = None

    def add_file(self, file: Path):
        if file not in self.files:
            self.files.append(file)

    def remove_file(self, file: Path):
        if file in self.files:
            self.files.remove(file)

    def clear_files(self):
        self.files.clear()
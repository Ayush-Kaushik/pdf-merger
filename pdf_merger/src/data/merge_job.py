# Author: Ayush Kaushik

from pathlib import Path
from dataclasses import dataclass, field
from typing import List


@dataclass
class MergeJob:
    """
    Domain model representing a merge task.
    Contains only state and simple domain rules.
    """

    files: List[Path] = field(default_factory=list)
    output_file: Path | None = None

    # ---------------------------------------------------------
    # FILE MANAGEMENT
    # ---------------------------------------------------------

    def add_file(self, file: Path) -> None:
        """Add a single file if not already present."""
        if file not in self.files:
            self.files.append(file)

    def add_files(self, paths: List[Path]) -> None:
        """Add multiple files."""
        for path in paths:
            self.add_file(path)

    def remove_file(self, file: Path) -> None:
        """Remove a file if present."""
        if file in self.files:
            self.files.remove(file)

    def clear_files(self) -> None:
        """Remove all input files."""
        self.files.clear()

    # ---------------------------------------------------------
    # OUTPUT TARGET
    # ---------------------------------------------------------

    def set_output_target(self, path: Path) -> None:
        """Set output file path."""
        self.output_file = path

    def clear_output_target(self) -> None:
        """Remove output target."""
        self.output_file = None

    # ---------------------------------------------------------
    # STATE HELPERS
    # ---------------------------------------------------------

    def has_files(self) -> bool:
        return len(self.files) > 0

    def file_count(self) -> int:
        return len(self.files)

    def has_output(self) -> bool:
        return self.output_file is not None

    def is_ready(self) -> bool:
        """
        Determine if the job can be executed.
        """
        return self.has_files() and self.has_output()

    # ---------------------------------------------------------
    # VALIDATION
    # ---------------------------------------------------------

    def validate(self) -> bool:
        """
        Validate merge job before execution.
        """
        if not self.is_ready():
            return False

        # ensure files exist
        for file in self.files:
            if not file.exists():
                return False

        return True

    # ---------------------------------------------------------
    # RESET
    # ---------------------------------------------------------

    def reset(self) -> None:
        """Reset the entire job."""
        self.clear_files()
        self.clear_output_target()
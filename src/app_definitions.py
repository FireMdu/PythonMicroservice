"""
This is a constant definitions
"""

from pathlib import Path

__all__ = [
    "PACKAGE_SOURCE_DIR",
    "ROOT_DIR"
]


PACKAGE_SOURCE_DIR: Path = Path(__file__).absolute().parent
ROOT_DIR: Path = PACKAGE_SOURCE_DIR.parent

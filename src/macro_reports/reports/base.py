from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable

from ..io.csv_reader import MacroRow


class Report(ABC):
    """Базовый класс для всех отчётов."""

    name: str

    @abstractmethod
    def build(self, rows: Iterable[MacroRow]):
        """Должен вернуть: headers, table_rows"""
        pass
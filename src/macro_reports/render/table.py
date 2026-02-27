from __future__ import annotations
from typing import Sequence, Any
from tabulate import tabulate


def print_table(headers: Sequence[str], rows: Sequence[Sequence[Any]]) -> None:
    """
    Печатает таблицу в консоль.
    """
    print(tabulate(rows, headers=headers, tablefmt="github"))
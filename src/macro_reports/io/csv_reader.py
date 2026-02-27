import csv
from dataclasses import dataclass
from pathlib import Path



@dataclass(frozen=True) #  приводим к красивому списку строк
class MacroRow:
    country: str
    year: int
    gdp: float


def read_rows(files: list[str]) -> list[MacroRow]:
    """
    Читаем CSV файлы и возвращаем список строк данных.
    """

    rows: list[MacroRow] = []

    for file_path in files:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        with path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)  # превращаем каждую строку CSV в отдельный словарь

            # каждая строка CSV будет словарем
            for r in reader:
                rows.append(
                    MacroRow(
                        country=r["country"],
                        year=int(r["year"]),
                        gdp=float(r["gdp"]),
                    )
                )

    return rows
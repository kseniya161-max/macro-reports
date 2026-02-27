from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from macro_reports.io.csv_reader import MacroRow
from macro_reports.reports.base import Report


@dataclass(frozen=True)
class AverageGDPReport(Report):
    """Считаем средний ВВП и сортируем по убыванию"""

    name: str = "average-gdp"

    def build(self, rows: Iterable[MacroRow]) -> tuple[list[str], list[list[object]]]:
        totals: dict[str, float] = {}
        counts: dict[str, int] = {}

        for r in rows:
            totals[r.country] = totals.get(r.country, 0.0) + float(r.gdp)
            counts[r.country] = counts.get(r.country, 0) + 1

        result_rows: list[list[object]] = []
        for country, total in totals.items():
            avg = total / counts[country]
            result_rows.append([country, round(avg, 2)])
        result_rows.sort(key=lambda x: x[1], reverse=True)

        headers = ["country", "avg_gdp"]
        return headers, result_rows
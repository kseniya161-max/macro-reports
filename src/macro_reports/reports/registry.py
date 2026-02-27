from __future__ import annotations

from dataclasses import dataclass

from macro_reports.reports.average_gdp import AverageGDPReport
from macro_reports.reports.base import Report


class UnknownReportError(ValueError):
    pass


def get_available_reports() -> list[str]:
    """
    Возвращает список имён отчётов.
    """
    return ["average-gdp"]


def get_report(report_name: str) -> Report:
    """
    По имени отчёта  возвращаем объект отчёта.
    """
    registry: dict[str, Report] = {
        "average-gdp": AverageGDPReport(),
    }

    report = registry.get(report_name)
    if report is None:
        available = ", ".join(get_available_reports())
        raise UnknownReportError(
            f"Unknown report: {report_name}. Available reports: {available}"
        )

    return report
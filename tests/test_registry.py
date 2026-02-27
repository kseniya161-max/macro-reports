import pytest

from macro_reports.reports.registry import (
    UnknownReportError,
    get_available_reports,
    get_report,
)


def test_get_available_reports_contains_average_gdp():
    assert "average-gdp" in get_available_reports()


def test_get_report_returns_report_instance_for_known_name():
    report = get_report("average-gdp")
    assert report.name == "average-gdp"


def test_get_report_raises_for_unknown_name():
    with pytest.raises(UnknownReportError):
        get_report("no-such-report")
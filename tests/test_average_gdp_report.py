from macro_reports.io.csv_reader import MacroRow
from macro_reports.reports.average_gdp import AverageGDPReport


def test_average_gdp_report_build_calculates_and_sorts_desc():
    rows = [
        MacroRow(country="A", year=2023, gdp=10),
        MacroRow(country="A", year=2022, gdp=30),
        MacroRow(country="B", year=2023, gdp=50),
    ]

    report = AverageGDPReport()
    headers, table_rows = report.build(rows)

    assert headers == ["country", "avg_gdp"]
    assert table_rows == [
        ["B", 50.0],
        ["A", 20.0],
    ]
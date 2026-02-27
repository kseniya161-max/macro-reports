from __future__ import annotations
import argparse
import sys
from pathlib import Path
from macro_reports.io.csv_reader import read_rows
from macro_reports.reports.registry import UnknownReportError, get_available_reports, get_report
from macro_reports.render.table import print_table


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """
    Разбирает аргументы командной строки.
    """
    parser = argparse.ArgumentParser(description="Macro reports CLI")

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files (one or more).",
    )


    parser.add_argument(
        "--report",
        required=True,
        help="Report name. Example: average-gdp",
    )

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """
    Точка входа CLI.
    """
    args = parse_args(argv)

    files = [str(Path(p)) for p in args.files]
    report_name = str(args.report)


    try:
        report = get_report(report_name)
    except UnknownReportError as e:

        print(str(e), file=sys.stderr)
        print(f"Available reports: {', '.join(get_available_reports())}", file=sys.stderr)
        return 2


    try:
        rows = read_rows(files)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 2


    headers, table_rows = report.build(rows)
    print_table(headers, table_rows)

    return 0
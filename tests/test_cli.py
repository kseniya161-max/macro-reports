from pathlib import Path

from macro_reports.cli import main


def _write_csv(path: Path) -> None:
    csv_content = (
        "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        "Spain,2023,100,0,0,0,0,Europe\n"
        "Spain,2022,300,0,0,0,0,Europe\n"
        "Mexico,2023,50,0,0,0,0,North America\n"
    )
    path.write_text(csv_content, encoding="utf-8")


def test_cli_success_prints_table_and_returns_0(tmp_path: Path, capsys):
    file_path = tmp_path / "data.csv"
    _write_csv(file_path)

    code = main(["--files", str(file_path), "--report", "average-gdp"])

    assert code == 0
    out = capsys.readouterr().out
    assert "country" in out
    assert "Spain" in out


def test_cli_unknown_report_returns_2(tmp_path: Path, capsys):
    file_path = tmp_path / "data.csv"
    _write_csv(file_path)

    code = main(["--files", str(file_path), "--report", "no-such-report"])

    assert code == 2
    err = capsys.readouterr().err
    assert "Unknown report" in err


def test_cli_missing_file_returns_2(capsys):
    code = main(["--files", "no_such_file.csv", "--report", "average-gdp"])

    assert code == 2
    err = capsys.readouterr().err
    assert "Файл не найден" in err
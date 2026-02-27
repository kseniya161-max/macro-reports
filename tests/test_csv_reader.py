from pathlib import Path
from macro_reports.io.csv_reader import read_rows


def test_read_rows_reads_csv_and_parses_types(tmp_path: Path):
    csv_content = (
        "country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n"
        "Spain,2023,1394,2.4,3.2,11.8,48,Europe\n"
        "Mexico,2022,1414,3.9,7.9,3.3,127,North America\n"
    )

    file_path = tmp_path / "economic.csv"
    file_path.write_text(csv_content, encoding="utf-8")

    rows = read_rows([str(file_path)])

    assert len(rows) == 2
    assert rows[0].country == "Spain"
    assert rows[0].year == 2023
    assert rows[0].gdp == 1394.0

    assert rows[1].country == "Mexico"
    assert rows[1].year == 2022
    assert rows[1].gdp == 1414.0
from macro_reports.render.table import print_table


def test_print_table_outputs_something(capsys):
    headers = ["country", "avg_gdp"]
    rows = [["Spain", 1409.33]]

    print_table(headers, rows)

    out = capsys.readouterr().out
    assert "country" in out
    assert "Spain" in out
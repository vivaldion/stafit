import os
from decimal import Decimal
from main import read_files, calc_avg, report


def test_read_files(sample_csv):
    """read file test"""
    data = read_files(sample_csv)
    assert len(data) == 5
    assert data[0]["country"] == "United States"
    assert data[0]["gdp"] == "25462"


def test_read_files_not_found():
    """non valid file"""
    data = read_files("nonexistent.csv")
    assert data == []


def test_calc_avg():
    """test avg calculate"""
    data = [
        {"country": "USA", "gdp": "100"},
        {"country": "USA", "gdp": "200"},
        {"country": "China", "gdp": "300"},
    ]
    result = calc_avg(data)

    assert len(result) == 2
    assert result["USA"] == Decimal("150")
    assert result["China"] == Decimal("300")


def test_report_sorted():
    """sorted"""
    data = {
        "A": Decimal("100"),
        "B": Decimal("300"),
        "C": Decimal("200"),
    }
    report_file = "test_sort.txt"

    report(data, report_file)

    with open(report_file, "r") as f:
        content = f.read()
        b_pos = content.find("B")
        c_pos = content.find("C")
        a_pos = content.find("A")
        assert b_pos < c_pos < a_pos

    os.unlink(report_file)


def test_integration(sample_csv):
    """fulltest"""

    data = read_files(sample_csv)
    assert len(data) == 5

    avg = calc_avg(data)
    assert len(avg) == 3
    assert avg["United States"] == Decimal("24388.5")
    assert avg["China"] == Decimal("17848.5")
    assert avg["Germany"] == Decimal("4086")

    report_file = "test_integration.txt"
    report(avg, report_file)
    assert os.path.exists(report_file)
    os.unlink(report_file)

import csv
from decimal import Decimal
from tabulate import tabulate
import argparse


def read_files(*file_paths):
    """gather data from files"""
    data = []
    for file in file_paths:
        try:
            with open(file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"file {file} not found error")
    return data


def calc_avg(data: list):
    """calculate avg"""
    country_data: dict[list] = {}
    for row in data:
        country = row["country"]
        gdp = row["gdp"]
        country_data.setdefault(country, []).append(gdp)

    avg_country_gdp = {}
    for country, values in country_data.items():
        values = [Decimal(x) for x in values]
        avg_gdp = sum(values) / len(values)
        avg_country_gdp[country] = avg_gdp
    return avg_country_gdp


def report(data: dict, report_file="average-gdp.txt"):
    """save report in file and output itpyt"""
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    headers = ["№", "country", "gdp"]
    table = [
        [number, country, f"{gdp}"]
        for number, (country, gdp) in enumerate(sorted_data, start=1)
    ]
    with open(report_file, "w", encoding="utf-8") as output:
        output.write(tabulate(table, headers=headers, tablefmt="grid", floatfmt=".2f"))
    print(tabulate(table, headers=headers, tablefmt="grid", floatfmt=".2f"))


def main():
    parser = argparse.ArgumentParser(description="macroeconomic data analyzes")
    parser.add_argument(
        "--files", nargs="+", required=True, help="csv files for calculating"
    )
    parser.add_argument(
        "--report", default="average-gdp.txt", help="report file- average-gdp.txt"
    )

    args = parser.parse_args()
    data = read_files(*args.files)
    if not data:
        print("No data loaded")
        return
    avg_gdp = calc_avg(data)
    report(avg_gdp, args.report)


if __name__ == "__main__":
    main()

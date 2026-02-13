import os
from tempfile import NamedTemporaryFile
import pytest


@pytest.fixture
def sample_csv():
    """temp csv file with data"""
    content = """country,year,gdp
United States,2023,25462
United States,2022,23315
China,2023,17963
China,2022,17734
Germany,2023,4086"""

    with NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".csv", delete=False
    ) as f:
        f.write(content)
        temp_file = f.name

    yield temp_file

    os.unlink(temp_file)
